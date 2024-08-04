import pandas as pd

mrktng = pd.read_csv('Marketing.csv')

# display the total non null values per column
print(mrktng.isnull().sum())

# display the null values of the DATA column
# in this example specifically the 'DATE'
print(mrktng[mrktng['Date'].isna()])

# getting rid of rows and columns with nulls
mrktng = mrktng.dropna()
print(mrktng.isnull().sum)

# display the summary statistics for all numeric columns
print(mrktng.describe())

# display the summary of a categorical/nominal data
# it will show the 
#   count = number or rows
#   unique = unique count of categories
#   top = the mode
#   freq = frequency of the top category
print(mrktng['Day_Name'].describe())

# filtering or slicing of data

# in this example we select all the data if the day is Monday
# by adding boolean condition to it
print(mrktng[mrktng['Day_Name'] == 'Monday'])

# select all the data when the day is Monday & Promo == 'No Promo'
# example 1 - 2 conditions
print(mrktng[(mrktng['Day_Name'] == 'Monday')
            & (mrktng['Promo'] == 'No Promo')])

# you can also sort values like revenue in descending order
# so top 5 values are at the top of the table
mrktng = mrktng.sort_values(by = 'Revenue', ascending = False).head(10)
print(mrktng.head(10))

# we can also display the sum or total 'revenue' per day
# option 1 - Series FORMAT  
print(mrktng.groupby('Day_Name')['Revenue'].sum())

# option 2 - Dataframe FORMAT (.agg or aggrigate method)
# this is better if you are planning to plot the results 
# for data visualizaation
print(mrktng.groupby('Day_Name', as_index = False).agg({'Revenue':'sum'}))

# create or add another missing column
mrktng['Revenue per Spend'] = mrktng['Revenue'] / mrktng['Marketing Spend']
print(mrktng.head())