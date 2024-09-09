import pandas as pd

# create a dataframe, sales, from csv file, all_sales.
sales = pd.read_csv("all_sales.csv")

sales.info()
print(sales.head())

# check the total number of blank rows
print(sales.isnull().sum())

# remove all nulls/blanks using the dropna() method.
sales = sales.dropna()
sales.info()
print(sales.isnull().sum())

# WHICH MONTH HAD THE HIGHEST SALE?
# WHICH PRODUCT SOLD THE MOST?
# HOW ARE THE OTHER PRODUCTS SOLD?
sales.info()
print(sales.head())
# WHAT IS THE MONTHLY SALES TREND?
# get the first two elements of the string of the order date to get the month since it is 04/19/19
sales['Month'] = sales['Order Date'].str[0:2]
print(sales.head())

# add the sales by month change the data type of the month column to an integer
#### sales = sales['Month'].astype('int32')
#### oh uh there is a value error 'Or' to fix this create a dump or dummy date frame to check 'Or's in the month column
Or_dump = sales[sales['Month']=='Or']
print(Or_dump.head())
#### then set a condition to not include them in a month column
sales = sales[sales['Month']!='Or']
#### then rerun to check
Or_dump = sales[sales['Month']=='Or']
print(Or_dump.head())
#### now lets change the data type again 
sales['Month'] = sales['Month'].astype('int32')
sales.info()
print(sales.head())

# sales column
# use to_numeric method to convert it to correct data type
sales['Quantity Ordered'] = pd.to_numeric(sales['Quantity Ordered'])
sales['Price Each'] = pd.to_numeric(sales['Price Each'])
sales.info()

# add sales column
sales['Sales'] = sales['Quantity Ordered']*sales['Price Each']
print(sales.head())
