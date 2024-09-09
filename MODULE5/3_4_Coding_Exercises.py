import pandas as pd

supermarket = pd.read_csv("supermarket_sales.csv")

supermarket.info()
print(supermarket.head())

print(supermarket.isnull().sum())

supermarket = supermarket.dropna()
print(supermarket.isnull().sum())

supermarket.info()