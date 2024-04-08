import pandas as pd

# create Dataframe from a list of dictionaries
data = [{'Alex',20},{'Bob',33},{'Claire',45}]
#df = pd.read_csv('.csv')

# assign column names
df= pd.DataFrame(data,columns=['Name','Age'])

print("Original DataFrame:")
print(df)
print(df.dtypes)

# Add a new column
new_column_data = ['Chicago', 'Miami', 'London']  
# Example data for the new column
df['City'] = new_column_data

# Display the DataFrame with the new column added
print("\nDataFrame with the new column:")
print(df)

# Add a new column
new_column_data = ['US', 'US', 'UK']  
# Example data for the new column
df['Country'] = new_column_data

# Display the DataFrame with the new column added
print("\nDataFrame with the new column:")
print(df)

df.to_csv("df_output.csv")


# create Dataframe from a list of dictionaries, row orientation
data = [
        {'Name':'Peter', 'Age':20, 'City':'Tempe'},
        {'Name':'Rebecca', 'Age':24, 'City':'Sheffield'},
        {'Name':'Louis', 'Age':21, 'City':'Paris'}
        ]
df2 = pd.DataFrame(data)
print(df2)

# create Dataframe from a dictionary of lists, column orientation
data = {
        'Name':['Peter','Rebecca', 'Louis'],
        'Age':[20,24,21],
        'City':['Tempe','Sheffield', 'Paris']
        }
df3 = pd.DataFrame(data)
print(df3)