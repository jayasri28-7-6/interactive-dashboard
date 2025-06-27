import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sales_data(num_samples=2000, filename='sales_data.csv'):
    """
    Generates a synthetic dataset for sales performance and saves it to a CSV file.

    Args:
        num_samples (int): The number of sales records to generate.
        filename (str): The name of the CSV file to save the data to.
    """
    print(f"--- Generating {num_samples} Synthetic Sales Data Samples ---")
    np.random.seed(42) # for reproducibility

    # Generate Dates
    start_date = datetime(2022, 1, 1)
    dates = [start_date + timedelta(days=np.random.randint(0, 730)) for _ in range(num_samples)] # Two years of data

    # Generate other features
    regions = ['North', 'South', 'East', 'West', 'Central']
    product_categories = ['Electronics', 'Clothing', 'Home Goods', 'Books', 'Food']

    data = {
        'Date': dates,
        'Region': np.random.choice(regions, num_samples),
        'ProductCategory': np.random.choice(product_categories, num_samples),
        'UnitsSold': np.random.randint(1, 20, num_samples),
        'PricePerUnit': np.random.uniform(10, 500, num_samples),
    }

    df = pd.DataFrame(data)

    # Calculate Sales and Profit
    df['Sales'] = df['UnitsSold'] * df['PricePerUnit'] + np.random.normal(0, 50, num_samples) # Add some noise
    df['Profit'] = (df['Sales'] * np.random.uniform(0.1, 0.4, num_samples)) - np.random.normal(0, 20, num_samples) # Profit with noise
    df['Profit'] = df['Profit'].apply(lambda x: max(1, x)) # Ensure profit is positive

    # Format Date column
    df['Date'] = pd.to_datetime(df['Date']).dt.date # Store as date object for simplicity

    df.to_csv(filename, index=False)
    print(f"Synthetic data saved to '{filename}'")
    print("\nDataset head:\n", df.head())
    print("\nDataset info:\n")
    df.info()
    print("\nDataset description:\n", df.describe())

if __name__ == "__main__":
    generate_sales_data()
