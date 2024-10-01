import pandas as pd

# Import CSV file into a DataFrame
df = pd.read_csv('chart.csv')  
print(df)

# a function to add a new column to the DataFrame
def add_new_column(df, column_name, values):
    df[column_name] = values

# Add new columns one by one
add_new_column(df, 'New_Column_1', [1, 2, 3])
add_new_column(df, 'New_Column_2', ['A', 'B', 'C'])

# Display the DataFrame after adding new columns
print(df)
#df.drop('Age', inplace=True, axis=1)
print(df)
df.to_csv("chart_new.csv")
