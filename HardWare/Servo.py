import time
import RPi.GPIO as GPIO


class Servo():

    frecuencia = 300
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
        self.p.ChangeDutyCycle(self.valor)

    def limpiarServo(self):
        GPIO.cleanup()

if __name__ == '__main__':

    servo1 = Servo(32)

    for i in range(100):
        servo1.writeServo(i)
        time.sleep(1)

    servo1.writeServo(0)
    servo1.limpiarServo()
        
    
    
    

    
    
