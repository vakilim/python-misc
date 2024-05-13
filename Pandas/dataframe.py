import pandas as pd
#Dataframe: 2d labeled data structure; has row and column index

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

#df.to_csv("df_output.csv")

# Creating a dataframe from a list, where each list represents a column
data_list = [['John', 25, 'Engineer'],
             ['Alice', 30, 'Manager'],
             ['Bob', 28, 'Analyst']]

df_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'Position'])

# Creating a dataframe from a dictionary (collection of key-value pairs). keys are column names.
data_dict = {'Name': ['John', 'Alice', 'Bob'],
             'Age': [25, 30, 28],
             'Position': ['Engineer', 'Manager', 'Analyst']}

df_dict = pd.DataFrame(data_dict)

print("Dataframe created from list:")
print(df_list)
print("\nDataframe created from dictionary:")
print(df_dict)

#Series: 1D labeled object; two arrays: one is index, the other the values
S = pd.Series([3,4,7,9,13,15,56])
S.name = "my_series"