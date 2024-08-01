import matplotlib.pyplot as plt
import statistics as stat
import pandas as pd

f_usage = [5, 4, 3, 5, 8, 2, 5, 2, 5, 8, 10, 8, 7, 9, 
           10, 5, 7, 5, 7, 5, 4, 3, 8, 4]

# EXAMPLE 1

# size of the graph
fig = plt.figure(figsize=(16,9))

# creating a histograph
plt.hist(f_usage, bins=8, edgecolor="black")

# labeling
plt.xlabel("Hours")
plt.ylabel("Frequency")
plt.title("Friends Social Media Usage")

# applying measure of central tendency and dispersion
# the first pair sets the value and the location of the line in the graph
# the second pair is for the lenght or the height of the line
# the last pair is for the line format
plt.plot([stat.mean(f_usage), stat.mean(f_usage)], [0,9], linestyle="--", color="r")
plt.plot([stat.mean(f_usage), stat.median(f_usage)], [0,10], linestyle="--", color="y")
plt.plot([stat.pstdev(f_usage), stat.pstdev(f_usage)], [0,9], linestyl="--", color="g")
plt.plot([stat.mode(f_usage), stat.mode(f_usage)], [0,9], linestyle="--", color="m")
plt.plot([stat.variance(f_usage), stat.variance(f_usage)], [0,9], linestyle="--", color="c")

# we can also add a block of text on the graph
plt.text(8,7,'mean', color="r")
plt.text(8,6,5,'median', color="y")
plt.text(8,6,'mode', color="m")
plt.text(8, 5.5,'std', color="g")
plt.text(8,5,'variance', color="c")

# to run the graph
plt.show
# EXAMPLE 2

# creating a horizontal bar graph
df = pd.read_csv("population_by_country_2020.csv")
sea_country = df[df["Country"].isin(["China", "South Korea", "North Korea", "Macau", 
                                        "Hong kong", "Tibet", "Taiwan", "Japan", "Mongolia"])]
fig = plt.figure(figure=(16,9))
country = sea_country['Country']
population = sea_country['Population (2020)']

plt.title("2020 Population by Country (SEA)", loc="center")
# simplest way to draw horizontal bar
plt.barh(country, population)

plt.show

fig, ax = plt.subplots(figsize=(16,9))

ax.barh(country, population)

ax.set_title("2020 Population by Country (SEA)", loc="center")

# removes axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

# add annotations to bars
for i in ax.patches:
    plt.text(i.get_width() + 0.2, i.get_y() + 0.5, str(round((i.get_width()), 2)), fontsize=10, fontweight="bold", color="grey")

# remove x, y ticks
ax.xaxis.set_ticks_position("none")
ax.yaxis.set_ticks_position("none")

# add padding / spaces between axes and labels
ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)

# add x, y gridlines
ax.grid(b=True, color="grey", linestyle="--", linewidth=0.5, alpha=0.2)

# show top values
ax.invert_yaxis()

plt.show