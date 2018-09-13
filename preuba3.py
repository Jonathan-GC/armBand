#!/usr/bin/python

from myo_raw_jonathan import *
band = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)
# ****************************************************

def proc_emg(emg, moving, times=[]):
    print(emg)
    ## print framerate of received data
    times.append(time.time())
    
    if len(times) > 20:
        #print((len(times) - 1) / (times[-1] - times[0]))
        times.pop(0)

def porc_imu(quat1, acc, gyro):
    #Covarianza
    cov  = [0,0,0,0,0,0,0,0,0]
    quat = "hola"

#*****************************************************
    
##band.add_emg_handler(proc_emg)
band.add_arm_handler(lambda arm, xdir: print('Brazo: ', arm, 'Direccion: ', xdir))
band.add_pose_handler(lambda p: print('Posicion', p))

band.connect()

while True:
    band.run()
    #band.tick()

