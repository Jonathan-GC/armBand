import time
import RPi.GPIO as GPIO

class KeyPad():

    #Variables para filtrar
    tiempo_validar=6
    tiempo_pasado=0

    ultimoEstadoBoton=0;
    estadoBoton = 0
    accionSalida=0
    pinIn = 0
    def __init__(self, pinIn):
        self.pinIn = pinIn
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pinIn, GPIO.IN)

    ##def __call__(self):
    ##    return self.ultimoEstadoBoton
        
    def dRead(self):
        lectura = GPIO.input(self.pinIn)
        
        if (lectura != self.ultimoEstadoBoton):
            self.tiempo_pasado = time.time()

        if ((time.time() - self.tiempo_pasado) > 0.1):

            if(lectura != self.estadoBoton):
                self.estadoBoton = lectura
                #print ("Accion que quiero")
                ##Accion que quiero
            
            if(self.estadoBoton == 1):
                print ("Accion que quiero")
                return True

        self.ultimoEstadoBoton=lectura


if __name__ == '__main__':

    btn_Selec=KeyPad(11)

    while True:
        btn_Selec.dRead()
        
        
    
