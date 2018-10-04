import time
import RPi.GPIO as GPIO
ledDigital = 19
ledAnalogo = 35

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledDigital, GPIO.OUT)
GPIO.setup(ledAnalogo,GPIO.OUT)

p = GPIO.PWM(ledAnalogo, 100)
# channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        
        for dc in range(0, 101, 1):
            #print(dc)
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        for dc in range(100, -1, -1):
            #print(dc)
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        
        
        '''
        print("LED on")
        GPIO.output(led,GPIO.HIGH)
        time.sleep(0.5)
        print("LED off")
        GPIO.output(led,GPIO.LOW)
        time.sleep(0.5)
        '''
except KeyboardInterrupt:
    pass
#p.stop()
GPIO.cleanup()