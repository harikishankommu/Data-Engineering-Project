import pandas as pd

# read raw dataset
df = pd.read_csv("../data/raw_sales.csv", encoding="latin1")

# remove duplicate rows
df = df.drop_duplicates()

# handle missing values
df = df.dropna()

# convert order date to datetime
if "ORDERDATE" in df.columns:
    df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

# create revenue column
if "QUANTITYORDERED" in df.columns and "PRICEEACH" in df.columns:
    df["REVENUE"] = df["QUANTITYORDERED"] * df["PRICEEACH"]

# save cleaned dataset
df.to_csv("../data/cleaned_sales.csv", index=False)

print("Data cleaned successfully")
print(df.head())