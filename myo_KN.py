#Librerias para el funcionamiento del ArmBand Myo
from __future__ import print_function
from collections import Counter, deque
import struct
import sys
import time

#Librerias para el tratamiento de Datos
import pandas as pd
import numpy as np

from sklearn import metrics
from sklearn import linear_model
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

#Libreria de Funcionamiento y extraccion de datos del Myo ArmBand
from common import *
from myo_raw_jonathan import MyoRaw

SUBSAMPLE = 3
K = 15



class CLassificador(object):
    
    #ojo con los clusters estos son lo que permiten el calculo perfecto de los datos
    clusters = 5
    clf = joblib.load('modeloEntrenado.pkl')
    
    #Contructor de inicio
    def __init__(self):
        pass
        
    #Funcion de almacenanmiento de datos paso (etiqueta, valor del sensor)
    def store_data(self, target, vals):
        with open("setDataCompleta.csv","a") as f:
            
            flag = str(vals) + ", " + str(int(target)) + "\n"
            flag = flag.replace("(","")
            flag = flag.replace(")","")
            f.write(flag)
                
            #f.close(); evito cerrarlo para que pueda agregar multiples datos

        #colocar Datos en los archivos
        
    def limpiar_data(self):
        #escribiendo nulo borro toda la data y efectivamente lo cierro
        with open("setDataCompleta.csv","w") as f:                      
            f.write("")
            f.close()
    
    def entrenar(self):
        try:
            #entablo el modelo de datos .pkl
            print("A entrenar")
            archivo = "setDataCompleta.csv"
            df = pd.read_csv(archivo)
        
            arregloX = df[df.columns[:-1]].values
            arregloy = df[df.columns[-1]].values 
            print(arregloX[len(arregloy)-2])
                                    
            '''
            Aqui colocaré el modelo de entrenamiento del modelo es importante lo hay:
                *Neigborhg supervisado,
                *lineal,
                *neuronal,
                *kmeans automatico
                *etc
            '''
            
            #MODELO CON BARRIOS CERCANOS FUNCIONA BIEN PERO LE FALTA PRESICION
                #X_train,X_test,y_train,y_test = train_test_split(arregloX, arregloy)
                #clf = KNeighborsClassifier(self.clusters)
                #clf.fit(X_train, y_train)      
                #print(clf.score(X_test, y_test))
            
            #MODELO CON Medias FUNCIONA MAL LE FALTA PRESICION
                ##km = KMeans(self.clusters, max_iter = 10000)
                ##km.fit(arregloX)
                ##predicciones = km.predict(arregloX)
                ##score = metrics.adjusted_rand_score(arregloy, predicciones)
                ##print(score)
            
            #MODELO CON REGRESION LINEAL FUNCIONA BIEN PERO LE FALTA PRESICION
            reg = linear_model.LogisticRegression()
            X_train,X_test,y_train,y_test = train_test_split(arregloX, arregloy)
            reg.fit(X_train,y_train)
            score = reg.score(X_test,y_test)
            print(score)
            
            ##Exportacion del modelo entrenado
            ##clf es la variable calsificador en este caso será km
            joblib.dump(reg,'modeloEntrenado.pkl')
        except ValueError:
            print("problemas para establecer el set de datos, intente de nuevo y Revise sus datos")

    def classify(self, d):
        try:
            return self.clf.predict([d])
        except ValueError:
            print("El modelo esta mal creado o las etiquetas no son suficientes de acuerdo a los nodos")
            return [0]

class Myo(MyoRaw):
    hist_len = 59

    def __init__(self, cls, tty=None):
        MyoRaw.__init__(self, tty)
        self.cls = cls

        self.history = deque([0] * Myo.hist_len, Myo.hist_len)
        self.history_cnt = Counter(self.history)
        self.add_emg_handler(self.emg_handler)
        self.last_pose = None

        self.pose_handlers = []

    def emg_handler(self, emg, moving):
        y = self.cls.classify(emg)
        #Quita un dato 
        self.history_cnt[self.history[0]] -= 1
        #Coloca el siguiente
        #y[] = dato entero que importa
        self.history_cnt[y[0]] += 1    
        self.history.append(y[0])
        #Tamaño del array siempre sera 25
        
        ##Desempaqueta el mas comun en el historial
        r, n = self.history_cnt.most_common(1)[0]
        
        if self.last_pose is None or (n > self.history_cnt[self.last_pose] + 5 and n > Myo.hist_len / 2):
            self.on_raw_pose(r)
            self.last_pose = r
        
    

    def add_raw_pose_handler(self, h):
        self.pose_handlers.append(h)

    def on_raw_pose(self, pose):
        for h in self.pose_handlers:
            h(pose)


if __name__ == '__main__':
    import subprocess
    m = Myo(CLassificador(), sys.argv[1] if len(sys.argv) >= 2 else None)
    m.add_raw_pose_handler(print)
  
   

    
    m.connect()

    try:
        while True:
            m.run()
        
    except KeyboardInterrupt:
        pass
        
    finally:
        m.disconnect()
        print()
