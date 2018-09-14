#!/usr/bin/python

from myo_raw_jonathan import *
import math
from io import open


band = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)

#Variables Publicas
publish_imu = []
publish_EMG = []
publish_Brazo = []

# ****************************************************


def escribirArchivo(archivo,vectorIn):
    
    print("Escribiendo Archivo")
    datos=open(archivo,"w")
    for element in vectorIn:
        flag = str(element)+"\n"
        datos.write(flag)
        
    datos.close()


def proc_emg(emg, moving, times=[]):
     
    publish_EMG.append(emg)
    times.append(time.time())
    if len(times) > 20:
        times.pop(0)

def imu_handler(quat, acc, gyro):
    
    ##Contante dadas por el fabricante
    scaleOrientacion = 16384.0    
    scaleAceleracion = 2048.0
    scaleGiro = 16.0
    
    
    q0, q1, q2,q3 = quat
    
    q0 = q0/scaleOrientacion
    q1 = q1/scaleOrientacion
    q2 = q2/scaleOrientacion
    q3 = q3/scaleOrientacion
    
    current_gyro = gyro
    current_accel = acc
    current_roll = math.atan2(2.0 * (q0 * q1 + q2 * q3), 1.0 - 2.0 * (q1 * q1 + q2 * q2))
    current_pitch = -math.asin(max(-1.0, min(1.0, 2.0 * (q0 * q2 - q3 * q1))))
    current_yaw = -math.atan2(2.0 * (q0 * q3 + q1 * q2), 1.0 - 2.0 * (q2 * q2 + q3 * q3))
 
    Vel=(((current_pitch)*180/math.pi)*2)-75 #ecuacion que define la vel del Jumpong
    Giro=(((current_roll)*180/math.pi))*0.6667 - 28.3333 #ecuacion que define la velocidad de giro
    
    vector_temp = current_gyro,current_accel,current_roll,current_pitch,current_yaw
    print(vector_temp)
    
    publish_imu.append(vector_temp)
    '''
    publish_imu.insert(1,current_accel)
    publish_imu.insert(2,current_roll)
    publish_imu.insert(3,current_pitch)
    publish_imu.insert(4,current_yaw)
    '''
#*****************************************************
    
band.add_emg_handler(proc_emg)
band.add_imu_handler(imu_handler)
band.add_arm_handler(lambda arm, xdir: print('Brazo: ', arm, 'Direccion: ', xdir))
#band.add_pose_handler(lambda p: print('Posicion', p))

band.connect()
try:
    cont = 0
    while cont <= 1000:
        band.run()
        cont += 1
        #print(cont)
        
        
finally:
    band.vibrate(3)
    band.disconnect()
    print("longitud EMG: ",len(publish_EMG))
    print("longitud IMU: ",len(publish_imu))


escribirArchivo("Datos IMU.txt",publish_imu)
escribirArchivo("Datos EMG.txt",publish_EMG)

print(publish_imu)
    


