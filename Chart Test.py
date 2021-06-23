import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("Netflixs/netflix_titles.csv")
datachart = (data[["release_year", "duration"]])
#data =sns.load_dataset("Netflixs/netflix_titles.csv")
fig, ax = plt.subplots()
sns.heatmap(datachart)
#sns.lineplot(x=data["director"].head(5), y=data["rating"].head(5), marker='o')

#plt.legend(loc='lower right')
# ax.plot(x,y)
plt.show()
