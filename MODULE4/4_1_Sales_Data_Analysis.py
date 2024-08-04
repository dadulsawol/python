# DATA ANALYSIS STEPS

# 1 Define the question/s.
# what is the yearly sales trend?
# which product sold the most in 2018?
# among the three product categoreis, which one had the lowest sale in 2018?
# what is the yearly sales trend of the three customer groups?
# are we getting more corporate customers?

# 2 Collect the Data
# The train dataset holds the sales data of an online office supplies and furniture shop from 2015 to 2018

# Clean the Data
# import pandas
import pandas as pd
# read the csv file 
train = pd.read_csv('train.csv')
# run .head() so we can take a look at the look of the first 5
print(train.head())
# run the info method so we can check how big our data frame is
print(train.info())
# run the .isnull().sum() method to check if there is any hole in this data frame 
print(train.isnull().sum())
# if there is a category with a missing value check it further with .isna() method
print(train[train['Postal Code'].isna()])
# since the null or blank is from one city example burlington removing this will affect the other data.
# we fill in the nulls with one of the postal code in burlington with non-null values using .fillna() method
train['Postal Code'] = train['Postal Code'].fillna('05401')
# then lets run again the .info() and .isnull() method
print(train.info())
print(train.isnull().sum())
# next check if there are any unnesseray columns this could be repeated data points or irrelevant data
# run the .head() method again
print(train.head())
# if found any you can delete a column using del keyword
del train['Row ID']
print(train.head(2))
# next important step of cleaning the data is checking the data type
# numeric data types are set as floats or integers
# nominal or categorical data are set as objects
# to easily work with dates it is also adviced to convert their data type to date time
# in the example the datatype of the order date, ship date and postal code is object
# to convert the object into date time we use .datetime() method
train['Order Date'] = pd.to_datetime(train['Order Date'], format='%d/%m/%Y')
train['Ship Date'] = pd.to_datetime(train['Ship Date'], format='%d/%m/%Y')
# converting float to object/string
train['Postal Code'] = train['Postal Code'].astype(str)
# then check the .info() method again
print(train.info())