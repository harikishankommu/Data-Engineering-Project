import pandas as pd

df = pd.read_csv("../data/raw_sales.csv", encoding="latin1")

print(df.head())