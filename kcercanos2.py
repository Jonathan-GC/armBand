import numpy as np
import sklearn
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


archivo = "DATOS.allSET.setDataCompleta.csv"
df = pd.read_csv(archivo)
print(df)