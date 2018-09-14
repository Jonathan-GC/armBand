#from __future__ import print_function

import sys
import time
from subprocess import Popen, PIPE
import re
import math
import time

from common import *
#importacion de datos de la myo desde el archivo myo_raw_jonathan
#varibles importadas
from myo_raw_jonathan import MyoRaw, Pose, Arm, XDirection 

class ArmBand(MyoRaw):
    
    def _init__(self, cls, tty = None):
        self.locked = True
        self.use_lock = True
        self.timed = True
        self.lock_time = 5.0
        self.time_to_lock = self.lock_time
        self.last_pose = -1
        self.last_tick = 0
        self.current_box = 0
        self.last_box = 0
        self.box_factor = 0.25
        self.current_arm = 0
        self.current_xdir = 0
        self.current_gyro = None
        self.current_accel = None
        self.current_roll = 0
        self.current_pitch = 0
        self.current_yaw = 0
        self.center_roll = 0
        self.center_pitch = 0
        self.center_yaw = 0
        self.first_rot = 0
        self.current_rot_roll = 0
        self.current_rot_pitch = 0
        self.current_rot_yaw = 0
        self.mov_history = ''
        self.gest_history = ''
        self.act_history = ''
        '''
        self.current_arm = 0
        self.current_xdir = 0
        self.current_gyro = None
        self.current_accel = None
        self.current_roll = 0
        self.current_pitch = 0
        self.current_yaw = 0
        self.current_rot = 0
        '''
        MyoRaw.__init__(self, tty)
        self.add_emg_handler(self.handler)
        self.add_arm_handler(self.arm_handler)
        self.add_imu_handler(self.imu_handler)
        self.add_pose_handler(self.pose_handler)
        
        self.onEMG = None
        self.onPoseEdge = None
        self.onLock = None
        self.onUnlock = None
        self.onPeriodic = None
        self.onWear = None
        self.onUnwear = None
        self.onBoxChange = None
        
	
    def vibrar(self, tipoVibracion):
        print("usted oprimio ", tipoVibracion)
        self.vibrate(tipoVibracion)
        pass
    
    def emg_handler(self,emg,moving):
        print(emg)
        if self.onEMG != None:
            self.onEMG(emg, moving)
    
    
    def arm_handler(self, arm, xdir):
        if arm == Arm(0):
            self.current_arm = 'Deconocido'
        elif arm == Arm(1):
            self.current_arm = 'Mano derecha'
        elif arm == Arm(2):
            self.current_arm = 'Mano Izquierda'

        if xdir == XDirection(0):
            self.current_xdir = 'unknown'
        elif xdir == XDirection(1):
            self.current_xdir = 'towardWrist'
	    	
        elif xdir == XDirection(2):
            self.current_xdir = 'towardElbow'
            
        if Arm(arm) == 0:
            if self.onUnwear != None:
                self.onUnwear()
        elif self.onWear != None:
            self.onWear(self.current_arm, self.current_xdir)	
		
if __name__ == '__main__':
        
    
    f = ArmBand(sys.argv[1] if len(sys.argv) >= 2 else None)
    f.connect()
    ##Aqui colocaré mis funciones haber como me va
    
    while True:
        
        #dato=int(input("Digite un valor: "))
        #no acepta interrupciones la funcion de vibrar, es curioso
        f.run()
        time.sleep(0.1)

        
        



