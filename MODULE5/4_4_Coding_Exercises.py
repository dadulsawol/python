import pandas as pd
import matplotlib.pyplot as plt
supermarket = pd.read_csv("supermarket_sales.csv")

# .isin() method
fig = plt.figure(figsize=(12,8))

bpayment_categories = ['Ewallet', 'Cash', 'Credit Card']
plt.subplot(1,2,1)
plt.bar(bpayment_categories,supermarket.groupby (['Payment']).sum()['Total'],color='grey')

plt.title('Sales by Payment')
plt.ylabel('Sales in Kyat (K)')
plt.ylim(0, 200000)

# .isin() method
bpayment_categories = ['Male', 'Female']
plt.subplot(1,2,2)
plt.bar(bpayment_categories,supermarket.groupby (['Gender']).sum()['Total'],color='grey')

plt.title('Sales by Gender')
plt.ylabel('Sales in Kyat (K)')
plt.ylim(0, 200000)

plt.show()
