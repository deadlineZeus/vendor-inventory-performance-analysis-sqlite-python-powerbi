import pandas as pd
import sqlite3
import logging
import os
import ingest_db  # your existing ingestion module

logging.basicConfig(
    filename="log/get_vendor_summary.log",
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def create_vendor_summary(conn):
    """Merge tables and create overall vendor summary with new calculated columns."""
    query = """
    WITH FreightSummary AS (
        SELECT 
            VendorNumber,
            SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),

    PurchaseSummary AS (
        SELECT
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price AS ActualPrice,
            pp.Volume,
            SUM(p.Quantity) AS TotalPurchaseQuantity,
            SUM(p.Dollars) AS TotalPurchaseDollars
        FROM purchase p
        JOIN purchase_prices pp ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume
    ),

    SalesSummary AS (
        SELECT
            VendorNo,
            Brand,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(SalesPrice) AS TotalSalesPrice,
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales
        GROUP BY VendorNo, Brand
    )

    SELECT
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        COALESCE(ss.TotalSalesQuantity, 0) AS TotalSalesQuantity,
        COALESCE(ss.TotalSalesDollars, 0) AS TotalSalesDollars,
        COALESCE(ss.TotalSalesPrice, 0) AS TotalSalesPrice,
        COALESCE(ss.TotalExciseTax, 0) AS TotalExciseTax,
        COALESCE(fs.FreightCost, 0) AS FreightCost
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss ON ps.VendorNumber = ss.VendorNo AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.TotalPurchaseDollars DESC
    """
    df = pd.read_sql_query(query, conn)
    return df

def clean_data(df):
    """Clean and enrich the vendor summary DataFrame."""
    df['Volume'] = df['Volume'].astype(float)

    df.fillna(0, inplace=True)

    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = df.apply(
        lambda x: (x['GrossProfit'] / x['TotalSalesDollars'] * 100) if x['TotalSalesDollars'] != 0 else 0, axis=1)
    df['StockTurnover'] = df.apply(
        lambda x: (x['TotalSalesQuantity'] / x['TotalPurchaseQuantity']) if x['TotalPurchaseQuantity'] != 0 else 0, axis=1)
    df['SalesToPurchaseRatio'] = df.apply(
        lambda x: (x['TotalSalesDollars'] / x['TotalPurchaseDollars']) if x['TotalPurchaseDollars'] != 0 else 0, axis=1)

    return df

if __name__ == "__main__":
    # Connect to SQLite database
    conn = sqlite3.connect('inventory.db')

    logging.info("Starting vendor summary creation...")
    summary_df = create_vendor_summary(conn)
    logging.info(f"Vendor summary created. Preview:\n{summary_df.head()}")

    logging.info("Cleaning vendor summary data...")
    clean_df = clean_data(summary_df)
    logging.info(f"Cleaned data preview:\n{clean_df.head()}")

    # Save cleaned DataFrame as temporary CSV
    temp_csv_path = "temp_vendor_summary.csv"
    clean_df.to_csv(temp_csv_path, index=False)
    logging.info(f"Temporary CSV saved at {temp_csv_path}")

    # Upload CSV to DB using ingest_db existing function
    ingest_db.upload_csv_to_db(temp_csv_path, ingest_db.engine)
    logging.info("Uploaded vendor summary CSV to database.")

    # Delete temporary CSV
    try:
        os.remove(temp_csv_path)
        logging.info(f"Temporary CSV file {temp_csv_path} deleted.")
    except Exception as e:
        logging.warning(f"Could not delete temporary CSV file: {e}")

    logging.info("Vendor summary processing completed.")
