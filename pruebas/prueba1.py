from myo_raw import  MyoRaw
import time
'''
def imprimaEmg(emg, moving, times=[]):

        print(emg)

        ## print framerate of received data
        times.append(time.time())
        if len(times) > 20:
            #print((len(times) - 1) / (times[-1] - times[0]))
            times.pop(0)
'''



brazalete = MyoRaw()
brazalete.connect()
brazalete.start_raw()
'''*OBTENCION'''
#brazalete.add_emg_handler(imprimaEmg)
#brazalete.add_emg_handler(lambda em, mov: print(mov))
#brazalete.add_pose_handler(lambda p: print(p))
#brazalete.add_arm_handler(lambda brazo, Xdirec : print(brazo, Xdirec))
#brazalete.add_imu_handler(lambda x,y,z: print(x))
'''''''''''''''
'''''''''''''''

#brazalete.vibrate(1)

mamaMolesta=brazalete.emg_handlers



if __name__ == '__main__':

    cont = 0
                
    try:
        while True:
            cont = cont + 1
            brazalete.run()
            brazalete.vibrate(1)
            brazalete.on_emg(lambda e,m: print(e))
            print(mamaMolesta)
            print("Joder tio ", cont)
            time.sleep(1)
    except:
        pass
                
    finally:
        brazalete.disconnect()
        print("Terminó")
            

