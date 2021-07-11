import pandas as pd
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
#Drop all rows that are duplicate
drop_duplicates= data.drop_duplicates()
print(data.shape,drop_duplicates.shape)

