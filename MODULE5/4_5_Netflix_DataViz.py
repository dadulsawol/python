import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('netflix_titles.csv')
print(df.head)
df.info()

# top 10 countries in netflix

movies_df = df[df['type'] == 'Movie']
top10Countries_movies = movies_df.groupby(['country']).size().sort_values(ascending=False)[0:10]

plt.figure(figsize=(12,6))
g = sns.barplot(x=top10Countries_movies.index, y=top10Countries_movies, color='grey')
g.text(0, 2200, 'Top 10 countries in Netflix movie production',
       fontsize=18, fontweight='bold', color='black')

for i in ['top', 'left', 'right']:
    g.spines[i].set_visible(False)

for i in g.patches:
    g.text(i.get_x()+i.get_width()/3.5,
           i.get_height()+60,
           round(i.get_height()),
           fontsize='18')
g.set(yticklabels=[])
plt.xlabel('')
plt.ylabel('')

plt.show()


tvshows_df = df[df['type'] == 'TV Show']
top10Countries_tvshows = tvshows_df.groupby(['country']).size().sort_values(ascending=False)[0:10]

plt.figure(figsize=(16,10))
# color='pastel' not working
g = sns.barplot(x=top10Countries_tvshows.index, y=top10Countries_tvshows)
g.text(0, 2200, 'Top 10 countries in Netflix TV Show production',
       fontsize=18, fontweight='bold', color='black')

for i in ['top', 'left', 'right']:
    g.spines[i].set_visible(False)

for i in g.patches:
    g.text(i.get_x()+i.get_width()/3.5,
           i.get_height()+60,
           round(i.get_height()),
           fontsize='18')
g.set(yticklabels=[])
plt.xlabel('')
plt.ylabel('')

plt.show()

# line graph

df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year
index = [2014, 2015, 2016, 2017, 2018, 2019, 2020]

# movies added from 2014 to 2020
ts_df = df[df['year_added']>2013]
ts_df = ts_df[ts_df['year_added']<2021].groupby('type')['year_added'].value_counts().unstack().T

fig, ax = plt.subplots(1,1, figsize=(12,6))
fig.text(0,15,1, 'Amount of Movies and TV Shows added over years',
         fontsize=18, fontweight='bold', color='black')

# line charts
g1 = sns.lineplot(x=ts_df.index, y = ts_df['Movie'], color='red', label='Movie')
g2 = sns.lineplot(x=ts_df.index, y = ts_df['TV Show'], color='red', label='TV Shows')

for i in ['top', 'left', 'right']:
    ax.spines[i].set_visible(False)

ax.legend(loc='upper left', frameon=False, prop={'size':15})
plt.xlabel(' ')
plt.ylabel(' ')

plt.show()