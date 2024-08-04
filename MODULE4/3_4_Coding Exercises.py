import pandas as pd

# series
authors = pd.Series(['E.L. James', 'Suzanne Collins', 
                    'J.K. Rowling', 'Dan Brown'])
reviews = pd.Series(['410', '211', '314', '178'])

print(authors)
print(reviews)

# data frame
dframe = {'authors': ['E.L. James', 'Suzanne Collins', 
                    'J.K. Rowling', 'Dan Brown'], 
          'reviews': ['410', '211', '314', '178']}
# easy way
# dframe = {'authors': authors, 'reviews': reviews}

# reading a csv in pandas
bestsellers = pd.read_csv('bestsellers.csv')

print(bestsellers.head(5))

print(bestsellers.info)
print(bestsellers.shape)