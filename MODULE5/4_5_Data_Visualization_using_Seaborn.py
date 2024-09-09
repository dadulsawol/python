import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
sns.set()
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

# STARTS HERE

#filter a table
table_group = sales.groupby('Product')
print(product_group.sum())

# .isin() method
hphone = sort_sum[sort_sum['Product'].isin(['Apple Airpods Headphones', 'Bose SoundSport Headphones', 'Wired Headphones'])]
print(hphone)

# with a graph
h_product = hphone['Product']
h_quantity = hphone['Quantity Ordered']

plt.bar(h_product, h_quantity)
plt.xticks(h_product, size=8)

plt.show()

# isin() method
phone = sort_sum[sort_sum['Product'].isin(['Google Phone', 'Vareebadd Phone', 'iPhone'])]
print(phone)

# with a graph
p_product = phone['Product']
p_quantity = phone['Quantity Ordered']

plt.bar(p_product, p_quantity)
plt.xticks(p_product, size=8)

# subplot method - putting two graphs together
# bar graph
fig = plt.figure(figsize=(16,10))

# plot 1 :
h_product = hphone['Product']
h_quantity = hphone['Quantity Ordered']

plt.subplot(1,2,1)
plt.bar(h_product, h_quantity)
plt.xticks(h_product, size=8)
# set a y limit to avoid confusing conclusion
plt.ylim(0, 22500)

# plot 2 :
p_product = phone['Product']
p_quantity = phone['Quantity Ordered']

plt.subplot(1, 2, 2)
plt.bar(p_product, p_quantity)
plt.xticks(p_product, size=8)
# set a y limit to avoid confusing conclusion
plt.ylim(0, 22500)

plt.show()

# subplot method - putting two graphs together
# barh graph
fig = plt.figure(figsize=(16,10))

# plot 1 :
h_product = hphone['Product']
h_quantity = hphone['Quantity Ordered']

plt.subplot(1,2,1)
plt.barh(h_product, h_quantity)
plt.yticks(h_product, size=8)
# set a y limit to avoid confusing conclusion
plt.xlim(0, 22500)

# plot 2 :
p_product = phone['Product']
p_quantity = phone['Quantity Ordered']

plt.subplot(1, 2, 2)
plt.barh(p_product, p_quantity)
plt.yticks(p_product, size=8)
# set a y limit to avoid confusing conclusion
plt.xlim(0, 22500)

plt.show()

# subplots() method - placing the values near the bars
fig, ax = plt.figure(figsize=(16,9))
product_group = sales.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

sort_sum = quantity_ordered.sort_values(ascending=True)
sort_sum = pd.DataFrame(sort_sum)
sort_sum = sort_sum.reset_index()

product = sort_sum['Product']
quantity = sort_sum['Quantity Ordered']

# calling the attributes of ax

# add y values to bars
for i in ax.patches:
    ax.text(i.get_width()+0.2, i.get_y()+0.5,
            str(round((i.get_width()), 2)),
            fontsize = 10, fontweight = 'bold',
            color = 'grey')

# remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# add x, y, gridlines
ax.grid(b=True, color='grey',
        linestyle=':')

# add padding/spaces between axes and labels
ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)

# remove axes spines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

plt.show()