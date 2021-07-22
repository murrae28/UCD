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


#Converting Margins % to whole numbers
data['GrossMarg'] = data['grossProfitMargin'] * 100
data['NetProf_Marg'] = data['netProfitMargin'] * 100
data['OpProf_Marg'] = data['operatingProfitMargin'] * 100
#print(data['GrossMarg'].head(5))

bar=data.groupby('Sector')["GrossMarg"].mean()
bar.plot(kind='bar', color = 'green',rot=45, fontsize=5)
plt.title('Gross Margin Avg per Sector', fontsize=14)
plt.show()

#Company_rating_A = data[["Name", "Rating"]]
#Company_rating_A.head()


print(data.loc[(data.Name == 'Whirlpool Corporation')])




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
print(data[['Name', 'Rating', 'debtEquityRatio', 'assetTurnover', 'netProfitMargin']])

#plt.bar(Company, 'grossProfitMargin')
#plt.show()

#extratcing the year from the date column
data['Year'] = pd.DatetimeIndex(data['Date']).year
print(data.Year)

sector_grouped = data.groupby('Rating').sum()[['GrossMarg','OpProf_Marg','NetProf_Marg']]
print(sector_grouped)
# define figure
fig, ax = plt.subplots(1, figsize=(16, 6))
# numerical x
x = np.arange(0, len(sector_grouped.index))
# plot bars
plt.bar(x - 0.3, sector_grouped['GrossMarg'], width = 0.2, color = '#1D2F6F')
plt.bar(x - 0.1, sector_grouped['OpProf_Marg'], width = 0.2, color = '#8390FA')
plt.bar(x + 0.1, sector_grouped['NetProf_Marg'], width = 0.2, color = '#ff1493')

# remove spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# x y details
plt.ylabel('Margin')
plt.xticks(x, sector_grouped.index)
#plt.xlim(5, 31)

# grid lines
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.2)

# title and legend
plt.title('Gross, OP, Net Profit Margins by Rating', loc ='left')
plt.legend(['NPM', 'OPM', 'GPM'], loc='upper left', ncol = 4)
plt.show()

plt.show()

avg_ratio_rating =pd.pivot_table(data, index =['Rating'], values = 'daysOfSalesOutstanding', aggfunc='mean')
print(avg_ratio_rating)
avg_ratio_rating.plot(kind='line')
plt.show()

## sort values
#Sector_grouped = data.sort_values('Sector')
sorted_data= data.sort_values(by=["Name", "Sector"])
sorted_data.sort_index(axis=1, ascending =False)
print(sorted_data.head())

Loop_index = [['Name', 'Sector', 'Rating']]

#for loop with a skipping with continue filter
Name_symbols = dict([['MMM', '3M Company'], ['ABB', 'ABB Ltd'], ['ACN', 'Accenture plc']])
Name_symbols['ACCO'] = 'Acco Brands Corporation'
for k in Name_symbols:
    if k =='ABB':
        continue
    print(k)

#Insight Focus on healthcare Sector
sector_data= data[(data.Sector == 'Health Care') & (data.Rating == 'CCC')]
print(sector_data[['Name', 'Rating', 'debtEquityRatio', 'assetTurnover', 'payablesTurnover']])

#Insight to AAA Ratings
best_rating = data[data['Rating'].str[2] == 'A']
print(best_rating[['Name', 'Rating', 'Rating Agency Name', 'Date','netProfitMargin', 'operatingProfitMargin', 'ebitPerRevenue', 'currentRatio', 'cashPerShare']])

#Insight to company AT&T
data.set_index("Name", inplace=True)
print(data.loc[['AT&T Inc.'], ['Rating', 'currentRatio', 'quickRatio', 'cashRatio']])













