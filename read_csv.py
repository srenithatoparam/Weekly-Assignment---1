import pandas as pd
from datetime import datetime

#read csv file
df = pd.read_csv("C:/Users/sreni/Downloads/sample.csv")

#After loading, check top rows and basic info
print(df.head())     # first 5 rows
print(df.shape)      # (rows, cols)
df.info()            # dtypes and non-null counts

#Simple cleaning: missing values, duplicates, bad rows
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print(f"Dropped {before-after} duplicate rows")

#Identify missing values:
print(df.isna().sum())   # count nulls per column

#change store names to uppercase
df['store_name'] = df['store_name'].str.strip().str.title()  # " store a " -> "Store A"
df['store_name'] = df['store_name'].str.upper()  # "Store A" -> "STORE A"

#Select only columns you need
df_small = df[['transaction_id', 'store_name', 'product_id', 'total']]

print(df_small)

#filter by store_name
store_a = df[df['store_name'] == 'AIRPORT']
print(store_a)

#filter by date range
start = '2025-10-04'
end   = '2025-10-05'
mask = (df['date'] >= start) & (df['date'] <= end)
df_range = df.loc[mask]
print(df_range)

#filter by high value transactions
high_value = df[df['total'] >= 7.0]   # transactions > 7
print(high_value)

#Combine filters (AIRPORT & high-value)
sf = df[(df['store_name'] == 'AIRPORT') & (df['total'] >= 7.0)]
print(sf)

#descriptive statistics & group summaries
print(df['total'].describe())

#totals by store
total_by_store = df.groupby('store_name')['total'].sum().reset_index().sort_values('total', ascending=False)
print(total_by_store)

#average basket per store
avg_by_store = df.groupby('store_name')['total'].mean().reset_index().sort_values('total', ascending=False)
print(avg_by_store)

#Transactions count per store
count_by_store = df.groupby('store_name')['transaction_id'].count().reset_index(name='Transactions')
print(count_by_store)

#daily sales trend (time series)
daily_sales = df.groupby('date')['total'].sum().reset_index()
print(daily_sales) 





