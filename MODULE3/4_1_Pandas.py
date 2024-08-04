# statistics using pandas

import pandas as pd

f_usage = [5, 4, 3, 5, 2, 5, 8, 10, 8, 7, 9, 
           10, 5, 7, 5, 7, 5, 4, 3, 8, 4]

# to get the mean count, std(for sample data), min, percentile/quartile, min/max
ser = pd.Series(f_usage)
sum_start = ser.describe()

print(sum_start)

# to get the standard deviation(for population) 
pstdeviation = ser.std(ddof=0)
print(pstdeviation)

# read file syntax of pandas (variable lang po si df)
df = pd.read_csv("./population_by_country_2020.csv")
print(f"ETO ANG AKING NABASA:", df)

# show the first 11
show_first = df.head(11)
print(show_first)

#show the last 11
show_last = df.tail(11)
print(show_last)

# setting a condition 
sel_country = df[df["Country"] == "Philippines"]
print(sel_country)

# WE USE .isin(10) method to filter our data set)
sel_SEA_country = df[df["Country"].isin(["Philippines", "Thailand", "Indonesia", 
                    "Myanmar", "Laos", "Vietnam", "Brunei", "Singapore", "Malaysia", "Cambodia", "Timor-Leste"])]
print(sel_SEA_country)

# we can also get summmary statistics using pandas
stat = sel_SEA_country["Population (2020)"].describe()
rstat = round(stat, 2)
print(rstat)

# we can also use this to rank the data
sel_SEA_country = df[df["Country"].isin(["Philippines", "Thailand", "Indonesia", 
                    "Myanmar", "Laos", "Vietnam", "Brunei", "Singapore", "Malaysia", "Cambodia", "Timor-Leste"])]
sort_sea = sea.sort_values(by="Population (2020)", ascending=False)
print(sort_sea)


# SI "my_venv" folder nasa loob siya ng "Python" folder. Punta ka lang po sa loob ng Python folder.
# Then run this script "my_venv/Scripts/activate"
# Then punta ka sa directory ng py file na gusto mo irun "MODULE4"
# Then "python 4_1_Pandas.py"