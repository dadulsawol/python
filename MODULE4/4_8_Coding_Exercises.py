import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

best = pd.read_csv('bestsellers.csv')

# Are the number of reviews increasing each year?
## CLEANING
best['Year'] = best['Year'].astype(str)
print(best.info())

yreviews = best.groupby('Year', as_index=False).agg({'Reviews':'sum'})
print(yreviews)

## PLOTTING
sns.lineplot(y='Reviews', x='Year', data = yreviews, marker='o')
plt.title('Reviews each Year')
plt.ylabel('Year')
plt.show()