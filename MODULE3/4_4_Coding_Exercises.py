# coding exercises

import pandas as pd

# read the file using pandas
df = pd.read_csv("./population_by_country_2020.csv")

# filter the data and display
display_country = df[df["Country"].isin(["China", "South Korea", "North Korea", "Macau", 
                                        "Hong kong", "Tibet", "Taiwan", "Japan", "Mongolia"])]
print(display_country)

# summary of the filtered data
filtered = display_country.describe()
print(filtered)