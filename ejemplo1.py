#!/usr/bin/env python
# -*- coding: utf-8 -*-

import myo_KN
from entrenando import posiciones
import sys
import struct
import time
from HardWare import Servo


#Variables Publicas
Servo1 = Servo.Servo(32) 



try:
    import pygame
    from pygame.locals import *
    HAVE_PYGAME = True
except ImportError:
    HAVE_PYGAME = False            


def setup():
    pass
    
        

if __name__ == '__main__':

    '''
    if HAVE_PYGAME:
        pygame.init()
        w, h = 900, 500
        scr = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Datos de Protesis SENA")
        font = pygame.font.Font(None, 30)
    '''

    m = myo_KN.Myo(myo_KN.CLassificador(), sys.argv[1] if len(sys.argv) >= 2 else None)
    
    m.connect()
    last_r = 0
    contador=0
    try:
        while True:
            m.run()
            r = m.history_cnt.most_common(1)[0][0]
        
            
            if r != last_r:
                print(r)
                last_r = r
                
                if r == 1:
                    Servo1.writeServo(50)
                elif r == 0:
                    Servo1.writeServo(180)
                elif r == 2:
                    Servo1.writeServo(0)
                elif r == 3:
                    Servo1.writeServo(20)
                elif r == 4:
                    Servo1.writeServo(100)
                elif r == 5:
                    Servo1.writeServo(90)
                
                #posiciones = ["Relajado","Puño","Señalar", "Pinza", "Meñique", "Abrir Mano"]    
                    
            
            
            
            '''
            if HAVE_PYGAME:
                
                scr.fill((0, 20, 0))#, (800, 0, 800, 320))
                text = "Protesis SENA"
                
                mensaje = font.render(text, 2, (50,255,255))
                scr.blit(mensaje,(15, 5))
                
                for ev in pygame.event.get():
                    if ev.type == QUIT or (ev.type == KEYDOWN and ev.unicode == 'q'):
                        raise KeyboardInterrupt()
                    elif ev.type == KEYDOWN:
                        if K_0 <= ev.key <= K_5:
                            contador +=1
                            print("Grabando posicion " + posiciones[ev.key-K_0] + " dato No: " + str(contador) )                          
                            hnd.recording = ev.key - K_0
                            
                        elif K_KP0 <= ev.key <= K_KP5:
                            hnd.recording = ev.key - K_Kp0
                        elif ev.unicode == 'r':
                            m.cls.entrenar()
                        elif ev.unicode == 'd':
                            m.cls.limpiar_data()
                    elif ev.type == KEYUP:
                        if K_0 <= ev.key <= K_5 or K_KP0 <= ev.key <= K_KP5:
                            hnd.recording = -1
                
                
               
                
                for i in range(len(posiciones)):
                    x = 0
                    y = (1 + i) * 40
                    

                    clr = (0,200,0) if i == r else (255,255,255)

                    txt = font.render(posiciones[i], True, (255,255,255))
                    scr.blit(txt, (x + 20, y))
                    

                    txt = font.render('%d' % i, True, clr)
                    scr.blit(txt, (x + 130, y))
                   
                    scr.fill((0,0,0), (x+145, y + txt.get_height() / 2 - 10, len(m.history) * 20, 20))
                    scr.fill(clr, (x+145, y + txt.get_height() / 2 - 10, m.history_cnt[i] * 20, 20))

                    
                
                
                
                
                pygame.display.flip()
                
               ''' 
                
    except KeyboardInterrupt:
        pass
        
    finally:
        m.disconnect()
        print()

    if HAVE_PYGAME:
        pygame.quit()


