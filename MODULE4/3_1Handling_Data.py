import pandas as pd

# creating a series by passing in a list
items = pd.Series(['chairs', 'labels', 'tables'])
print(items)

# creating a series by passing in a list with an indexcd folder_name
items = pd.Series(['chairs', 'labels', 'tables'], index=['OR 001', '0R 002', 'OR 003'])
print(items)

# creating a series by passing in a list with an index
names = pd.Series(['Joe', 'Tom', 'Jane'])
print(names)

# creating data frame 
# data frame is a collection of series or columns
dframe = {'Name': ['Joe', 'Tom', 'Jane'],
          'items': ['chairs', 'labels', 'tables']}
purchases = pd.DataFrame(dframe)
print(purchases)

# loading CSV file into a DATAFRAME 
mdata = pd.read_csv('Marketing.csv')

# runs the first 5 rows
print(mdata.head())

# runs the number of rows you select
print(mdata.head(10))

# runs the last 5 rows
print(mdata.tail())

# runs the number of last rows select
print(mdata.tail(10))

# display the first rows and the information of the dataframe
print(mdata.info())
print(mdata.head())

# display the shape, number of columns and rows in the data
print(mdata.shape)