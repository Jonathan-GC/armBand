import numpy as np
import sklearn
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib

clusters=9

archivo = "setDataCompleta.csv"
df = pd.read_csv(archivo)
arregloX = df[df.columns[:-1]].values
arregloy = df[df.columns[-1]].values  #as_matrix()

X_train,X_test,y_train,y_test = train_test_split(arregloX, arregloy)
clf = KNeighborsClassifier(clusters)
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))


##Exportacion del modelo entrenado
joblib.dump(clf, 'modeloEntrenado.pkl')

'''
k = knn.predict([[80, 94,341,265,300,156,90,10]])
print(k)
'''