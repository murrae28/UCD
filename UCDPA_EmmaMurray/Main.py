import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests

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
#Creating subset for only A rated companies
Only_A= data[data['Rating'] == 'A']
print(Only_A.head())

data['GrossMarg'] = data['grossProfitMargin'] * 100
print(data['GrossMarg'].head(5))

bar=data.groupby('Sector')["GrossMarg"].mean()
bar.plot(kind='bar', rot=45)
plt.show()

#Company_rating_A = data[["Name", "Rating"]]
#Company_rating_A.head()




print(data.loc[(data.Name == 'Whirlpool Corporation') & (data.Rating == 'AAA')])
data.plot(x='Rating', y='cashPerShare', kind ='line', rot=45)
plt.show()



#Counting ratings by company name
print(data.groupby(['Name', 'Rating'], as_index=False).Rating.count())
#plt.bar('Rating', 'Sector')
#plt.show()

sector_grouped = data.groupby('Sector').sum()[['grossProfitMargin','operatingProfitMargin','netProfitMargin']]
print(sector_grouped)


data_sector =data.loc[data['Sector'] == 'Finance']
Company= ['Equifax, Inc.', 'Marsh & McLennan Companies, Inc.', 'Aon plc', 'S&P Global Inc.', 'Progressive Corporation (The)', 'Loews Corporation']
data.loc[data['Name'].isin(Company)]
print(data.head())
print(data.shape)
#plt.bar(Company, 'grossProfitMargin')
#plt.show()

#extratcing the year from the date column
data['Year'] = pd.DatetimeIndex(data['Date']).year
print(data.Year)

sector_grouped = data.groupby('Rating').sum()[['freeCashFlowPerShare','cashPerShare']]
print(sector_grouped)
# define figure
fig, ax = plt.subplots(1, figsize=(16, 6))
# numerical x
x = np.arange(0, len(sector_grouped.index))
# plot bars
plt.bar(x - 0.3, sector_grouped['freeCashFlowPerShare'], width = 0.2, color = '#1D2F6F')
#plt.bar(x - 0.1, sector_grouped['operatingProfitMargin'], width = 0.2, color = '#8390FA')
plt.bar(x + 0.1, sector_grouped['cashPerShare'], width = 0.2, color = '#6EAF46')

# x y details
#plt.ylabel('Percentage')
plt.xticks(x, sector_grouped.index)

plt.show()

avg_ratio_rating =pd.pivot_table(data, index =['Rating'], values = 'currentRatio', aggfunc='mean')
print(avg_ratio_rating)

data['GrossMarg'] = data['grossProfitMargin'] * 100
print(data['GrossMarg'].head(5))

bar=data.groupby('Sector')["GrossMarg"].mean()
bar.plot(kind='bar', rot=45)
plt.show()

#for i in (Company):
    #print(i)
    #if i == '*z':
        #break



