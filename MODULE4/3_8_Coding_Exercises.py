import pandas as pd

best = pd.read_csv('Bestsellers.csv')
print(best.head())

# checking the summary of null info
print(best.info())
print(best.isnull().sum())

# checking the nulls in name which makes it unneccessary as there is no name
print(best[best['Name'].isna()])

# deleting nulls and checking the summary of null info
best = best.dropna()
print(best.isnull().sum())

# getting data information after cleaning it
print(best.info())
print(best.head())

# delete type column
del best['Type']
print(best.head())

#  Are the number of reviews increasing each year?
print(best.groupby('Year', as_index=False).agg({'Reviews':'sum'}))

# Which book received the most number of views?
best = best.sort_values(by = 'Reviews', ascending = False)
print(best.head(10))
