import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
supermarket = pd.read_csv("supermarket_sales.csv")

supermarket.info()
print(supermarket.head())

print(supermarket.isnull().sum())

supermarket = supermarket.dropna()
print(supermarket.isnull().sum())

supermarket.info()

supermarket_group = supermarket.groupby('Payment')
sns.set()
pcategories = ['Cash', 'Credit Card', 'Ewallet']
plt.bar(pcategories, supermarket.groupby(['Payment']).sum()['Total'])
plt.title("Sales by Payment")
plt.ylabel("Sales in Kyat (K)")
plt.xlabel(' ')
plt.show()

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

fig = plt.figure(figsize=(12,8))

product_line = supermarket.groupby('Product line')
quantity = product_line.sum()['Quantity']

sort_sum = quantity.sort_values(ascending=True)
sort_sum = pd.DataFrame(sort_sum)
sort_sum = sort_sum.reset_index()

product = sort_sum['Product line']
quantity = sort_sum['Quantity']

g = sns.barplot(x=product, y=quantity, palette='pastel')

for i in ['top', 'left', 'right']:
    g.spines[i].set_visible(False)

for i in g.patches:
    g.text(i.get_x()+i.get_width()/3.5,
        i.get_height()+5,
        round(i.get_height()),
        fontsize='14')


plt.xlabel(' ')
plt.ylabel(' ')
plt.show()