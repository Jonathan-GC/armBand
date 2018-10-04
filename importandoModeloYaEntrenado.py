import pandas as pd
from sklearn.externals import joblib


archivo = "setDataCompleta.csv"
df = pd.read_csv(archivo)
arregloX = df[df.columns[:-1]].values
arregloy = df[df.columns[-1]].values  #as_matrix()


clf = joblib.load('modeloEntrenado.pkl')
print(clf.score(arregloX,arregloy))

