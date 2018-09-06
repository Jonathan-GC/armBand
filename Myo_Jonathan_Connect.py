from __future__ import print_funtion
import sys
import time
import math
from common import *
from myo_raw import MyoRaw, Pose, Arm, XDirecction

class ArmBand(MyoRaw):
	self.current_arm = 0
	self.current_xdir = 0
	self.current_gyro = None
	self.current_accel = None
	self.current_roll = 0
	self.current_pitch = 0
	self.current_yaw = 0
	self.current_rot = 0

	MyoRaw.__init__(self, tty)
	self.add_emg_handler(self.handler)
	self.add_arm_handler(self.arm_handler)
	self.add_imu_handler(self.imu_handler)
	self.add_pose_handler(self.pose_handler)

	def.vibrar(self, tipoVibración)
		self.vibrate(tipoVibración)


