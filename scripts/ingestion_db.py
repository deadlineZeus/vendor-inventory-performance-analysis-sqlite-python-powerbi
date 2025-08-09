import sqlite3
import os
import pandas as pd
import logging
import time
from sqlalchemy import create_engine, inspect, text

# === Create logging directory and setup ===
os.makedirs('log', exist_ok=True)
log_file = os.path.join('log', 'logging.log')

logging.basicConfig(
    filename=log_file,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# === Create SQLite DB engine in E: drive ===
engine = create_engine('sqlite:///E:/sqlite_db/inventory.db')
inspector = inspect(engine)


def normalize_path(path_str):
    """
    Normalize and return a cleaned path string.
    Handles forward and backward slashes.
    """
    return os.path.normpath(path_str.strip())


def get_csv_files(directory):
    """
    Returns a list of full paths to CSV files in the given directory.
    Displays full shape of each CSV before proceeding.
    """
    directory = normalize_path(directory)
    try:
        all_files = os.listdir(directory)
        csv_files = [file for file in all_files if file.lower().endswith('.csv')]
        if not csv_files:
            print("No CSV files found in the directory.")
            return []

        print(f"\nFound {len(csv_files)} CSV files:\n")
        for file in csv_files:
            path = os.path.join(directory, file)
            try:
                df = pd.read_csv(path)
                print(f"{file}  →  Shape: {df.shape}")
            except Exception as e:
                print(f"{file}  →  [Could not read file: {e}]")
                logging.warning(f"Could not read full shape of {file}: {e}")

        return [os.path.join(directory, file) for file in csv_files]

    except Exception as e:
        logging.error(f"Error reading directory {directory}: {e}")
        print(f"Error reading directory: {e}")
        return []


def drop_table_if_exists(table_name, engine):
    """
    Drops the table if it already exists in the SQLite database.
    """
    if inspector.has_table(table_name):
        try:
            with engine.connect() as conn:
                conn.execute(text(f"DROP TABLE IF EXISTS '{table_name}'"))
                logging.info(f"Table '{table_name}' existed and was dropped.")
        except Exception as e:
            logging.error(f"Failed to drop table '{table_name}': {e}")


def upload_csv_to_db(file_path, engine, chunk_size=100000):
    """
    Uploads a CSV file to the SQLite database.
    Replaces the table if it already exists.
    Handles large files using chunked upload.
    Displays total time taken in human-readable format.
    """
    table_name = os.path.splitext(os.path.basename(file_path))[0]
    try:
        file_size_mb = os.path.getsize(file_path) / (1024 ** 2)
        print(f"\nUploading: {os.path.basename(file_path)} ({file_size_mb:.2f} MB)")
        logging.info(f"Started uploading {file_path} into table '{table_name}'")

        start_time = time.time()

        # Drop existing table
        drop_table_if_exists(table_name, engine)

        # Use chunked read for large files
        if file_size_mb > 100:
            for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size)):
                chunk.to_sql(table_name, con=engine, if_exists='append', index=False)
                logging.info(f"Inserted chunk {i+1} into '{table_name}'")
        else:
            df = pd.read_csv(file_path)
            df.to_sql(table_name, con=engine, if_exists='replace', index=False)

        end_time = time.time()
        total_time = end_time - start_time

        # Format time display
        if total_time < 1:
            time_str = f"{total_time:.2f} seconds"
        elif total_time < 60:
            time_str = f"{total_time:.2f} seconds"
        else:
            minutes = int(total_time // 60)
            seconds = int(total_time % 60)
            time_str = f"{minutes} minute{'s' if minutes != 1 else ''} {seconds} second{'s' if seconds != 1 else ''}"

        print(f"Successfully uploaded '{table_name}' in {time_str}.")
        logging.info(f"Finished uploading '{table_name}' in {time_str}.")

    except Exception as e:
        print(f"Failed to upload {file_path}: {e}")
        logging.error(f"Error uploading {file_path}: {e}")


def upload_all_csvs(directory):
    """
    Orchestrates the CSV upload process:
    1. Lists all CSVs with shape
    2. Uploads to SQLite
    3. Replaces existing tables if needed
    """
    csv_paths = get_csv_files(directory)
    if not csv_paths:
        print("No valid CSV files to upload.")
        return

    for path in csv_paths:
        upload_csv_to_db(path, engine)

        
if __name__ == '__main__':
    upload_all_csvs(r'C:\Users\Rajdeep Ray\Desktop\Vendor Performance Analysis & Optimization')
    
    

# Connect to your SQLite database
conn = sqlite3.connect('E:/sqlite_db/inventory.db')

# Query to get all table names
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [row[0] for row in cursor.fetchall()]

# Display the table names
print("Tables in the SQLite database:")
for table in tables:
    print("-", table)