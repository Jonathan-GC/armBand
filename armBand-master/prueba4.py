#!/usr/bin/python
import sys
from myo_raw_jonathan import *
import math
from io import open
#from pykeyboard import PyKeyboard

#import fcntl
#fd= sys.stdin.fileno()
#flags= fcntl.fcntl(fd,fcntl.F_GETFL)
#fcntl.fcntl(fd, fcntl.F_SETFL, flags|os.O_NONBLOCK)

#pTeclado = PyKeyboard()
band = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)

#Variables Programa
flag = 'r'


#Variables Publicas
publish_imu = []
publish_EMG = []
publish_Brazo = []

normQuat = []
normACC = []
normGyro = []
poseActual = ""

# ****************************************************
def posicion_Actual(poses):
    #print(poses)
    poseActual = poses.name
    #str(poseActual)
    print(poseActual)
  
    
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
    
    ##Desempaqueta el Vector quat, acc, gyro
    q0, q1, q2,q3 = quat
    accX, accY, accZ = acc
    giroX, giroY, giroZ = gyro


    ##Escala el quaternion 
    q0 = q0/scaleOrientacion
    q1 = q1/scaleOrientacion
    q2 = q2/scaleOrientacion
    q3 = q3/scaleOrientacion

    
    ##tranlasion del acc y giro para usos futuros
    current_gyro = gyro
    current_accel = acc
    ##Calculos de giro, Alabeo y cabeceo
    current_roll = math.atan2(2.0 * (q0 * q1 + q2 * q3), 1.0 - 2.0 * (q1 * q1 + q2 * q2))
    current_pitch = -math.asin(max(-1.0, min(1.0, 2.0 * (q0 * q2 - q3 * q1))))
    current_yaw = -math.atan2(2.0 * (q0 * q3 + q1 * q2), 1.0 - 2.0 * (q2 * q2 + q3 * q3))

    ##Saca la normal del vector y lo escala
    quatNorm = math.sqrt(q0*q0 + q1*q1 + q2*q2 + q3*q3)
    normQuat = q0/quatNorm, q1/quatNorm, q2/quatNorm, q3/quatNorm
    normACC = accX/scaleAceleracion, accY/scaleAceleracion, accZ/scaleAceleracion
    normGyro = giroX/scaleGiro, giroY/scaleGiro, giroZ/scaleGiro


    Vel=(((current_pitch)*180/math.pi)*2)-75 #ecuacion que define la vel del Jumpong
    Giro=(((current_roll)*180/math.pi))*0.6667 - 28.3333 #ecuacion que define la velocidad de giro
    
    ##LA tabla de salida será:
    ##[[quat],[gyro],[accel],giro,alabeo,cabeceo, [normalAcel], [normalGyro]]
    vector_temp = quat, current_gyro,current_accel,current_roll,current_pitch,current_yaw,normACC,normGyro
    
    ##Anexa en el timesTamp al Vector
    publish_imu.append(vector_temp)

#*****************************************************
    
band.add_emg_handler(proc_emg)
band.add_imu_handler(imu_handler)
band.add_arm_handler(lambda arm, xdir: print('Brazo: ', arm, 'Direccion: ', xdir))
band.add_pose_handler(posicion_Actual)
#band.add_pose_handler(lambda p: print('Posicion', p))

if __name__ == '__main__':
    band.connect()
    try:
        
        while flag == 'r':
            band.run()
            if sys.stdin.read(1)=='f':
                #if tecla == 'n':
                band.vibrate(1)
                flag = 'c'
            #    print("presiono: ", tecla, " chao...")
               
            #poseActual = band.add_pose_handler(posicion_Actual)
            #print(poseActual)
            #if poseActual == "PUNIO":
            #    contador = 1
            #    print("entra aquie")
            
    except KeyboardInterrupt:
        pass        
            
    finally:
        band.vibrate(3)
        band.disconnect()
        print("longitud EMG: ",len(publish_EMG))
        print("longitud IMU: ",len(publish_imu))


    escribirArchivo("Datos IMU.txt",publish_imu)
    escribirArchivo("Datos EMG.txt",publish_EMG)

    print(publish_imu)
        


