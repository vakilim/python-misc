"""
An example of Pandas DataFrame.

Taken from https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe
"""

import pandas as pd

data = [['Alex',20],['Bob',33],['Claire',45]]
#df = pd.read_csv('.csv')
df= pd.DataFrame(data,columns=['Name','Age'])

print("Original DataFrame:")
print(df)
print(df.dtypes)

# Add a new column
new_column_data = [1, 2, 3]  
# Example data for the new column
df['Kids'] = new_column_data

# Display the DataFrame with the new column added
print("\nDataFrame with the new column:")
print(df)

# Add a new column
new_column_data = ['m', 'm', 'f']  
# Example data for the new column
df['Sex'] = new_column_data

# Display the DataFrame with the new column added
print("\nDataFrame with the new column:")
print(df)

df.to_csv("df_output.csv")

