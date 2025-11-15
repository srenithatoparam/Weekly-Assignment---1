import pandas as pd

def read_csv(source):
    if source.startswith("http"):
        df = pd.read_csv(source)
    else:
        df = pd.read_csv(source)
    return df

def clean_data(df):
    # Trim strings and normalize category names
    if 'store_name' in df.columns:
        df['store_name'] = df['store_name'].astype(str).str.strip().str.title()

    # Convert Date
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Clean Amount
    if 'total' in df.columns:
        df['total'] = df['total'].astype(str).str.replace('[\$,]', '', regex=True)
        df['total'] = pd.to_numeric(df['total'], errors='coerce')

    # Drop rows without essential values
    df = df.dropna(subset=['transaction_id','store_id'])
    # Drop duplicates
    df = df.drop_duplicates()
    return df

def transform_data(df):
    # Example transform: add Year, Month, Day columns
    df['Year'] = df['date'].dt.year
    df['Month'] = df['date'].dt.month
    df['Day'] = df['date'].dt.day

    # Example aggregate: totals by store & month
    agg = df.groupby(['store_name', 'Year', 'Month'])['total'].agg(['sum', 'mean', 'count']).reset_index()
    agg = agg.rename(columns={'sum': 'TotalSales', 'mean': 'AvgBasket', 'count': 'TransactionCount'})
    return df, agg

def write_json(df, out_path):
    # Save full cleaned data
    df.to_json(out_path, orient='records', date_format='iso')

def write_aggregates_json(agg, out_path):
    agg.to_json(out_path, orient='records')

if __name__ == "__main__":
    source = "C:/Users/sreni/Downloads/sample.csv"
    df = read_csv(source)
    df = clean_data(df)
    df, agg = transform_data(df)
    write_json(df, 'cleaned_transactions.json')
    write_aggregates_json(agg, 'store_monthly_aggregates.json')
    print("ETL completed, outputs written:")
    print(" - cleaned_transactions.json")
    print(" - store_monthly_aggregates.json")

    #A short hands-on test
    assert df['total'].isna().sum() == 0, "There should be no missing Amounts"
    assert df['date'].dtype == 'datetime64[ns]', "Date column should be datetime"
    # Check totals sum consistency
    raw_total = df['total'].sum()
    agg_total = agg['TotalSales'].sum()
    assert abs(raw_total - agg_total) < 1e-6, "Aggregates should sum to raw totals"
    print("Basic tests passed")

