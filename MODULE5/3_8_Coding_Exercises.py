import pandas as pd
import matplotlib.pyplot as plt
supermarket = pd.read_csv("supermarket_sales.csv")

supermarket.info()
print(supermarket.head())

print(supermarket.isnull().sum())

supermarket = supermarket.dropna()
print(supermarket.isnull().sum())

supermarket.info()

supermarket_group = supermarket.groupby('Payment')

pcategories = ['Cash', 'Credit Card', 'Ewallet']
plt.bar(pcategories, supermarket.groupby(['Payment']).sum()['Total'])
plt.title("Sales by Payment")
plt.ylabel("Sales in Kyat (K)")
plt.xlabel(' ')
plt.show()