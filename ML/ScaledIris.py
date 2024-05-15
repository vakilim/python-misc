from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import numpy as np

# Load the iris dataset
iris = load_iris()
X = iris.data

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit the scaler to the data and transform it
X_scaled = scaler.fit_transform(X)

# Print the mean and standard deviation of the scaled data
print("Mean of each feature after scaling:", np.mean(X_scaled, axis=0))
print("Standard deviation of each feature after scaling:", np.std(X_scaled, axis=0))
#axis = 0 means operate along the columns (i.e., down the rows); mean/std of each column
