import pandas as pd

#This will read the excel file
df = pd.read_excel('Rotten_Tomatoes_data_score.xlsx')

#This will display the dataframe
print(df)

#To access specific columns
column_data = df['Box_Office', 'Year']
print(column_data)

#Access specific Row
row_data = df.iloc[0:]
print(row_data)