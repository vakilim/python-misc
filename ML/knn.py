from sklearn.neighbors import KNeighborsClassifier
#from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset (150 data points)
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Targets

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#train_data, test_data, train_labels, test_labels = datasets
#datasets = train_test_split(iris.data, iris.target, test_size=0.2)
#20% of 150 are tested

# Create a KNN classifier with k=3
knn = KNeighborsClassifier(n_neighbors=3)

"""
clf = MLPClassifier(solver = 'lbfgs',
                    alpha = 1e-5,
                    hidden_layer_sizes=(8,),
                    random_state=1)
"""

# Train the classifier
knn.fit(X_train, y_train) #train_data, train_labels

# Make predictions on the test data
y_pred = knn.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

