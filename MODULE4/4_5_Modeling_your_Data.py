# DATA ANALYSIS STEPS

# 1 Define the question/s.
# what is the yearly sales trend?
# which product sold the most in 2018?
# among the three product categories, which one had the lowest sale in 2018?
# what is the yearly sales trend of the three customer groups?
# are we getting more corporate customers?

# Answer the questions
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('train.csv')
print(train.head())

# First Question?
# the order should be by year, CREATE a order year column
# use .dt.year method
train['Order Date'] = pd.to_datetime(train['Order Date'], format='%d/%m/%Y')
train['Order Year']=train['Order Date'].dt.year
print(train.info()) 
print(train.head())

train['Order Year'] = train['Order Year'].astype(str)

# to change a category in sting or integer use .astype(str) method
train['Order Year'] = train['Order Year'].astype(str)
print(train.info())

# now get the sum of sales by year using grouby and agg method
# place the values to a new data frame example "ysales"
ysales = train.groupby('Order Year', as_index= False).agg({'Sales':'sum'})
print(ysales)

# Second Question?
sales_2018 = train[train['Order Year'] == '2018']
print(sales_2018)  

product_sales = sales_2018.groupby('Product Name', as_index=False).agg({'Sales':'sum'})
p = sales_2018.sort_values(by='Sales', ascending = False)
print(p.head(10))

# Third Question?

lowest_sale = sales_2018.groupby('Category', as_index = False).agg({'Sales':'sum'})
print(lowest_sale.sort_values(by='Sales', ascending= False).head(10))

# Fourth Question?
consumer_segment = train[train['Segment'] == 'Consumer']
consumer = consumer_segment.groupby('Order Year', as_index= False).agg({'Sales':'sum'})
print(consumer)

home_segment = train[train['Segment'] == 'Home']
home = home_segment.groupby('Order Year', as_index= False).agg({'Sales':'sum'})
print(home)

corporate_segment = train[train['Segment'] == 'Corporate']
corporate = corporate_segment.groupby('Order Year', as_index= False).agg({'Sales':'sum'})
print(corporate)

# QUESTION 1
# plotting a graph
# LINE GRAPH
sns.lineplot(x='Order Year', y='Sales', data=ysales, marker="o")
plt.xlabel(' ')
plt.show()

# QUESTION 2
# BAR GRAPH HORIZONTAL
# first limit the result 
p_top = p[(p['Sales']>=4416.174)]
sns.barplot(y='Product Name', x='Sales', data=p_top, orient='h', color='grey', errorbar=('ci', False))
plt.title('Top Products in 2018')
plt.ylabel(' ')
plt.show()

# QUESTION 3
# BAR GRAPH VERTICAL
sns.barplot(x='Category', y='Sales', data=lowest_sale, palette='Blues', hue='Category', legend=False)
plt.title('Sales by Product Category')
plt.xlabel(' ')
plt.ylabel(' ')
plt.show()

# QUESTION 4
# LINE GRAPH WITH MULTIPLE LINES
sns.lineplot(x='Order Year', y='Sales', data = consumer, marker='o')
sns.lineplot(x='Order Year', y='Sales', data = home, marker='o')
sns.lineplot(x='Order Year', y='Sales', data = corporate, marker='o')
plt.legend(['Consumer', 'Home', 'Corporate'])
plt.show()