from myo_raw import MyoRaw
import time

store = ["usted", "si" , "jode"]


joder = MyoRaw()
joder.connect()

joder.start_raw()
joder.mc_end_collection()
store = joder.emg_handlers
store1 = joder.imu_handlers
store2 = joder.add_imu_handler(lambda x, y, z: print())
##print("x: ",x, "Y: ", y, "Z: ", z))



print(type(store1))

def desencadenar(h):
    for datos in h:
        print(h)


try:
    while True:
    
        joder.run()
        print("EMG ", store)
        print("IMU", store1)
               
    
        time.sleep(1)
except:
    pass

finally:
    joder.disconnect()
    print("Termino")
    desencadenar(store1)

# p, este objeto se crea en la linea 207, recibe el paquete que viene del bluethoot
# hay unos datos de emg y moving, que se pueden globalizar y tratar en lineas 280 y 281
#mc_start_collection =Desabilita gyros, pero habilita la lista de posiciones y handlres
#mc_end_collection = lo que hace es rehjabiliotar las posiciones y el gyro a la vez
