import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Netflixs/netflix_titles.csv")

x= data["country"].head(5)
y= data["rating"].head(5)

fig,ax=plt.subplots()
ax.plot(x,y)
plt.show()

