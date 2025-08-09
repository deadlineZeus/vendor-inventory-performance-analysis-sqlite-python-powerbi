import pandas as pd
import sqlite3
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="log/get_vendor_summary.log",
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def create_vendor_summary(conn):
    """this function will merge the different tables to get the overall vendor summary and adding new columns in the resultant data"""
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary AS (
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
        JOIN purchase_prices pp
            ON p.Brand = pp.Brand
        WHERE p.PurchasPrice > 0
        GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume),

    SalesSummary AS (
        SELECT
            VendorNo,
            Brand,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(SalesPrice) AS TotalSalesPrice,
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales
            GROUP BY VebdorNo, Brand
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
                        ss.TotalSalesQuantity,
                        ss.TotalSalesDollars,
                        ss.TotalSalesPrice,
                        ss.TotalExciseTax,
                        fs.FreightCost
                    FROM PurchaseSummary ps
                    LEFT JOIN SalesSummary ss
                        ON ps.VendorNumber = ss.VendorNo
                        AND ps.Brand = ss.Brand
                    LEFT JOIN FreightSummary fs
                        ON ps.VendorNumber = fs.VendorNumber
                    ORDER BY ps.TotalPurchaseDollars DESC)""", conn)
    
    return vendor_sales_summary

def clean_data(df):
    """this function will clean the data"""
    #changing the datatype to fload
    df['Volume'] = df['Volume'].astype('float')

    #filling the missing values woth 0
    df.fillna(0, inplate=True)

    #removing white spaces from mcategorical columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    #creating new columns for better analysis
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = df['GrossProfit']/df['TotalSalesDollars']*100
    df['StockTurnover'] = df['TotalSalesQuantity']/df['TotalPurchaseQuantity']
    df['SalesToPurchaseRatio'] = df['TotalSalesDollars']/df['TotalPurchaseDollars']

    return df

if __name__ == __main__:

    #creating database connection
    conn=sqlite3.connect('inventory.db')

    logging.info('Creating Vendor summary table...')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleaning data....')
    clead_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting data...')
    ingest.db(clean_df, 'vendor_sales_summary', conn)
    logging.info('Completed')