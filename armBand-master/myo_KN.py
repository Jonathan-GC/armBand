from __future__ import print_function
from collections import Counter, deque
import struct
import sys
import time

import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


from common import *
from myo_raw_jonathan import MyoRaw

SUBSAMPLE = 3
K = 15
'''
class NNClassifier(object):
    #fabricacion de los archivos.dat con la informacion de
    los datos de entrenamiento

    def __init_(self):
        
        for i in range(10):
            with open('vals%d.csv' % i, 'r') as f: pass
        self.read_data()

    def almacene_data(self, cls, vals):
        with open('vals%d.dat' % cls, 'w') as f:
            f.write(pack('8H', *vals))

        #X_train,X_test,y_train,y_test = train_test_split(iris['data'], iris['target'])

    def leer_data(self):
        X=[]
        Y=[]
        ##entrenelo
'''

class CLassificador(object):
    knn = 0

    def __init__(self):
        knn = KNeighborsClassifier(n_neighbors=10)
        

    def classify(self, d):
        if self.X_test.shape[0] < K * SUBSAMPLE: return 0
        return knn.predict([[d]])


class Myo(MyoRaw):
    hist_len = 25

    def __init__(self, cls, tty=None):
        MyoRaw.__init__(self, tty)
        self.cls = cls

        self.history = deque([0] * Myo.hist_len, Myo.hist_len)
        self.history_cnt = Counter(self.history)
        self.add_emg_handler(self.emg_handler)
        self.last_pose = None

        self.pose_handlers = []

    def emg_handler(self, emg, moving):
        #y=emg
        y = self.cls.classify(emg)
        #Quita un dato 
        self.history_cnt[self.history[0]] -= 1
        #Coloca el siguiente
        self.history_cnt[y] += 1
        self.history.append(y)
        
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
    m = Myo(sys.argv[1] if len(sys.argv) >= 2 else None)
    m.add_raw_pose_handler(print)
    
    def page(pose):
        if pose == 5:
            subprocess.call(['xte', 'key Page_Down'])
        elif pose == 6:
            subprocess.call(['xte', 'key Page_Up'])

    m.add_raw_pose_handler(page)

    
    m.connect()

    while True:
        m.run()
