import numpy as np
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X_train,X_test,y_train,y_test = train_test_split(iris['data'], iris['target'])
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))
k = knn.predict([[1.2,3.4,5.6,1.1]])
print(k)
