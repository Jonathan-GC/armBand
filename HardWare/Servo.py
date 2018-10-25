import time
import RPi.GPIO as GPIO


class Servo():
    ##Encontré esta frecuencia y me parecio la idel para mi servo
    ##MG995 Tower PRO
    #Voy a usar una frecuencia de 50Hz es la ideal
    frecuencia = 50 
    p = 0
    #Estas variables se dan luego de buscar un valor que me diera 180 y 90 grados
    #con un valor en bits, por lo tanto con este se calculara la pendiente M en el inicio
    val_min = 2.9
    val_max = 10.9
    M=0

    def __init__(self,pinOUT):
        
        self.M = (self.val_max - self.val_min)/180
        
        self.pinOUT = pinOUT
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pinOUT, GPIO.OUT)
        self.p = GPIO.PWM(self.pinOUT, self.frecuencia)
        self.p.start(self.val_min)

    def writeServo(self, valor):
        self.valor = valor
        if 180 <= self.valor:
            self.valor = 180
        elif self.valor < 0:
            self.valor = 0
        
        ##Aqui esta la linealizacion para que de valores mucho mas exactos
        ##Como se ve tiene la forma X=mx + b
        self.valor = (self.M * self.valor) + self.val_min
        self.p.ChangeDutyCycle(self.valor)
        
        
    def limpiarServo(self):
        self.p.stop()

if __name__ == '__main__':

    try:
        servo1 = Servo(32)
        while True:
            
            
            for i in range(0,181,5):
                print(i)
                servo1.writeServo(i)
                time.sleep(0.5)
            
            
            
            #servo1.limpiarServo()
    except KeyboardInterrupt:
        pass

    finally:
        servo1.limpiarServo()
    
            
    
    
    

    
    
