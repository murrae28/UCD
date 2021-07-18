import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importing file from kaggle
data=pd.read_csv("corporate_rating.csv")

#running small checks to determine size of dataset
print(data.head())
print(data.shape)

#checking for missing values
missing_values_count = data.isnull().sum()
print(missing_values_count[0:5])

#If missing data is detecting, drop entire row
droprows= data.dropna()
print(data.shape,droprows.shape)
print(data[:3])

#Drop all rows that are duplicate
drop_duplicates= data.drop_duplicates()
print(data.shape,drop_duplicates.shape)

#Identifying what rows have a A type rating
is_a_rating=print(data['Rating'].isin(['A', 'AA', 'AAA']))
Rating_A =['A', 'AA', 'AAA']

print(data.loc[(data.Name == 'Whirlpool Corporation') & (data.Rating == 'AAA')])

#Counting ratings by company name
print(data.groupby(['Name', 'Rating']).Rating.count())

data =data.loc[data['Sector'] == 'Finance']
Company= ['Equifax, Inc.', 'Marsh & McLennan Companies, Inc.', 'Aon plc', 'S&P Global Inc.', 'Progressive Corporation (The)', 'Loews Corporation']
data.loc[data['Name'].isin(Company)]
print(data.head())
print(data.shape)
#extratcing the year from the date column
data['Year'] = pd.DatetimeIndex(data['Date']).year
print(data.Year)




#avg_ratio_rating =pd.pivot_table(data, index =['Name'], columns='Rating', values = 'currentRatio', aggfunc='mean')
#print(avg_ratio_rating)








