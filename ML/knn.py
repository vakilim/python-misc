from sklearn.neighbors import KNeighborsClassifier
#from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset (150 data points)
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#train_data, test_data, train_labels, test_labels = datasets
#datasets = train_test_split(iris.data, iris.target, test_size=0.2)
#20% of 150 are tested

# Create a KNN classifier with k=3
knn = KNeighborsClassifier(n_neighbors=5)

"""
clf = MLPClassifier(solver = 'lbfgs',
                    alpha = 1e-5,
                    hidden_layer_sizes=(8,),
                    random_state=1)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
"""

# Train the classifier (fit the model to the training data)
knn.fit(X_train, y_train) #train_data, train_labels

# Predict the labels for the test data
y_pred = knn.predict(X_test)

print("Predictions from the classifier:")
print(knn.predict(X_test))
print("Target values:")
print(y_test)

# Evaluate the accuracy of the classifier (predictions, labels)
accuracy = accuracy_score(y_test, y_pred)
#print("Accuracy:", accuracy)
print(f"Accuracy: {accuracy*100:.2f}%")
print(f"{accuracy:.2f}")

print("\n")

print(f"Prediction: {knn.predict(X_test[-15:,:])}")
print(f"Actual:     {y_test[-15:]}")
print('Accuracy: %.3f' % knn.score(X_test, y_test) )

print("\n")

for k in [1, 3, 5, 7, 10, 50, 100]:
    kNN = KNeighborsClassifier(n_neighbors=k)
    kNN.fit(X_train, y_train)
    test_score = kNN.score(X_test, y_test)
    print(f"k= {k:3} \t accuracy= {test_score:.3f}")
