"""
CSV Shuffler & Sampler
----------------------
This script processes all CSV files in a given directory:
1. Shuffles the records randomly.
2. Limits the output to a maximum of 1000 rows.
3. Saves processed files into a 'processed' subdirectory.

Author: Rajdeep Ray
Date: 09/08/2025
"""

import os
import pandas as pd


def shuffle_and_sample_csvs(folder_path: str, max_rows: int = 1000) -> None:
    """
    Shuffle and sample CSV files from the given folder.

    Parameters
    ----------
    folder_path : str
        Path to the folder containing CSV files.
    max_rows : int, optional
        Maximum number of rows to keep in each output CSV (default is 1000).
    """
    # Validate input folder
    if not os.path.isdir(folder_path):
        print(f"ERROR: Invalid folder path: {folder_path}")
        return

    print(f"Selected folder: {folder_path}")

    # Create output folder
    processed_folder = os.path.join(folder_path, "processed")
    os.makedirs(processed_folder, exist_ok=True)

    # Identify CSV files
    csv_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".csv")]
    if not csv_files:
        print("No CSV files found in the selected folder.")
        return

    print(f"Found {len(csv_files)} CSV file(s): {csv_files}")

    # Process each CSV
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        print(f"\nProcessing file: {csv_file}")

        try:
            # Load CSV
            df = pd.read_csv(file_path)
            print(f"  Records loaded: {len(df)}")

            # Shuffle
            df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)
            print("  Records shuffled.")

            # Limit rows
            if len(df_shuffled) > max_rows:
                df_shuffled = df_shuffled.head(max_rows)
                print(f"  Trimmed to {max_rows} rows.")
            else:
                print(f"  No trimming needed ({len(df_shuffled)} rows).")

            # Save processed file
            output_path = os.path.join(
                processed_folder, f"{os.path.splitext(csv_file)[0]}_sample.csv"
            )
            df_shuffled.to_csv(output_path, index=False)
            print(f"  Saved to: {output_path}")

        except Exception as e:
            print(f"  ERROR processing {csv_file}: {e}")

    print("\nAll CSV files processed successfully.")
    print(f"Processed files are saved in: {processed_folder}")


# ---------------- MAIN EXECUTION ---------------- #
if __name__ == "__main__":
    folder_path_input = input("Enter the path to the folder containing CSV files: ").strip()
    shuffle_and_sample_csvs(folder_path_input)
