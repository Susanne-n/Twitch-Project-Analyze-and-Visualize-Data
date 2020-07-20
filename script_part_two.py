import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# in this part of the project you will be taking your findings from the SQL queries and visualize them using Python and Matplotlib

# Bar Graph: Top 10 Most Popular Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]
viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

plt.bar(range(len(games)), viewers, color = 'blue')
plt.title('Viewers per game')
plt.legend(['Twitch'])
plt.xlabel('Most Popular Games')
plt.ylabel('Number of Views')
ax = plt.subplot()
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games)
plt.show()

plt.clf()

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]
countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(countries, explode=explode, colors=colors, autopct = '%1.0f%%', pctdistance=1.1)
plt.axis('equal')
plt.title("League of Legends Viewers' Whereabout")
plt.legend(labels, loc=5)
plt.subplots_adjust(right=1)
plt.show()

plt.clf()

# Line Graph: Time Series Analysis

hour = range(24)
viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

plt.plot(hour, viewers_hour)
plt.title('US viewers per hour')
plt.xlabel('Hours')
plt.ylabel('Number of Viewers per Hour')
plt.legend(['2015-01-01'])
ax = plt.subplot()
ax.set_xticks(hour)
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])

# some people leave their browsers open, account for 15% error in the viewers_hour data
y_upper = [x + x*0.15 for x in viewers_hour]
y_lower = [x - x*0.15 for x in viewers_hour]
plt.fill_between(hour, y_upper, y_lower, alpha = 0.2)

plt.show()
