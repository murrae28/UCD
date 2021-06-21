import pandas as pd

data = pd.read_csv("Netflixs/netflix_titles.csv")

new_data = data.drop_duplicates(subset=["director", "cast"])

print(data.shape, new_data.shape)


