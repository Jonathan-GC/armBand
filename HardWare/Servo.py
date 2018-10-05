import time
import RPi.GPIO as GPIO


class Servo():
    ##Encontré esta frecuencia y me parecio la idel para mi servo
    ##MG995 Tower PRO
    frecuencia = 450
    p = 0

    def __init__(self,pinOUT):

        self.pinOUT = pinOUT
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pinOUT, GPIO.OUT)
        self.p = GPIO.PWM(self.pinOUT, self.frecuencia)
        self.p.start(0)

    def writeServo(self, valor):
        self.valor = valor
        if 180 <= self.valor:
            self.valor = 100
        elif self.valor < 0:
            self.valor = 0
        
        ##Aqui esta la linealizacion para que de valores mucho mas exactos
        ##Como se ve tiene la forma X=mx + b
        #self.valor = (39/90)*self.valor + 0
        self.valor = (5/9)*self.valor + 0
        flag = int(self.valor)
        #print(flag)
        self.p.ChangeDutyCycle(flag)

    def limpiarServo(self):
        self.p.stop()

if __name__ == '__main__':

    try:
        servo1 = Servo(32)
        while True:
            
            
            for i in range(0,180,5):
                print(i)
                servo1.writeServo(i)
                time.sleep(0.5)
            
            
            
            #servo1.limpiarServo()
    except KeyboardInterrupt:
        pass

    finally:
        servo1.limpiarServo()
    
            
    
    
    

    
    
