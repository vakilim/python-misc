import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Load the California housing dataset
housing_data = fetch_california_housing()
X = housing_data.data
y = housing_data.target

# Split the dataset into training and testing sets
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a StandardScaler object
scaler = StandardScaler()

# Fit the scaler to the training data and transform the data
#X_train_scaled = scaler.fit_transform(X_train)
X_scaled = scaler.fit_transform(X)

"""
# Transform the test data using the same scaler
X_test_scaled = scaler.transform(X_test)

# Train the linear regression model on the scaled data
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Print the coefficients
print("Coefficients:", model.coef_)
"""

# Train the linear regression model on the scaled data
model = LinearRegression()
model.fit(X_scaled, y)

# Print the beta coefficients (values of b in y=bx+a)
print("Coefficients:", model.coef_)