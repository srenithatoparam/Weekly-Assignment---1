import pandas as pd
from datetime import datetime

#Create a DataFrame from Python lists/dicts
data = {
    "Date": ["12/11/2025","13/11/2025"],
    "Store": ["Store A", "Store B"],
    "TransactionID": [1001, 1002],
    "Amount": ["45.50", "120.99$"],
    "PaymentType": ["Card", "Cash"]
}
df2 = pd.DataFrame(data)
print(df2)

#Check dtypes
print(df2.dtypes)

#If date is a string, convert it to datetime
df2['Date'] = pd.to_datetime(df2['Date'], errors='coerce')  # converts to datetime; invalid => NaT

print(df2)

# Example: remove dollar sign/comma then convert
df2['Amount'] = df2['Amount'].astype(str).str.replace('[\$,]', '', regex=True)
df2['Amount'] = pd.to_numeric(df2['Amount'], errors='coerce')  # invalid -> NaN
print(df2)
