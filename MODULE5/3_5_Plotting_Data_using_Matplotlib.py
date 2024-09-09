import pandas as pd
import matplotlib.pyplot as plt
sales = pd.read_csv("all_sales.csv")

sales.info()
print(sales.head())
print(sales.isnull().sum())

sales = sales.dropna()
sales.info()
print(sales.isnull().sum())

sales.info()
print(sales.head())
sales['Month'] = sales['Order Date'].str[0:2]
print(sales.head())

Or_dump = sales[sales['Month']=='Or']
print(Or_dump.head())

sales = sales[sales['Month']!='Or']

Or_dump = sales[sales['Month']=='Or']
print(Or_dump.head())

sales['Month'] = sales['Month'].astype('int32')
sales.info()
print(sales.head())

sales['Quantity Ordered'] = pd.to_numeric(sales['Quantity Ordered'])
sales['Price Each'] = pd.to_numeric(sales['Price Each'])
sales.info()

sales['Sales'] = sales['Quantity Ordered']*sales['Price Each']
print(sales.head())

# WHICH MONTH HAD THE HIGHEST SALE?
# WHAT IS THE MONTHLY SALES TREND?

# BAR GRAPH
months = range(1,13)
# to remove the exponential marker just divide it by 1000000 or 1M
plt.bar(months,sales.groupby(['Month']).sum()['Sales']/1000000)

plt.title("Monthly Sales 2019")
plt.ylabel("Sales in USD")
plt.xlabel("Months")

# to complete the markers on the X axis by adding xticks with the months variable as the parameter
plt.xticks(months)
plt.show()

# LINE GRAPH
# make the graph bigger using fig
fig = plt.figure(figsize = (10,6))
months = range(1,13)
# to remove the exponential marker just divide it by 1000000 or 1M
# change the graph line color
plt.plot(months,sales.groupby(['Month']).sum()['Sales']/1000000, color='orange')

# setting the font size
plt.title("Monthly Sales 2019", fontsize=14, fontweight='bold')
plt.ylabel("Sales in USD", fontsize=12, color='green')
plt.xlabel("Months", fontsize=12, color='green')

# to complete the markers on the X axis by adding xticks with the months variable as the parameter
plt.xticks(months)

# add grid
plt.grid(True, color='grey', linestyle=':')

# change the color of the label and remove the spines too
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.show()

# WHICH PRODUCT SOLD THE MOST?
# HOW ARE THE OTHER PRODUCTS SOLD?

# use group by method
product_group = sales.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

products = [product for product, df in product_group]

# horizontal column bar
plt.barh(products, quantity_ordered)

plt.title("Total Units Sold", fontsize=12)
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.yticks(products)
plt.show()

# improving the readability of the graph
fig = plt.figure(figsize=(16,10))
product_group = sales.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

sort_sum = quantity_ordered.sort_values(ascending=True)
sort_sum = pd.DataFrame(sort_sum)
sort_sum = sort_sum.reset_index()

product = sort_sum['Product']
quantity = sort_sum['Quantity Ordered']

plt.barh(products, quantity)

plt.xlabel("Units Sold")
plt.yticks(products, size=10)

plt.grid(True, color='grey',linestyle=':')
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.show()