#!/usr/bin/env python
# -*- coding: utf-8 -*-

import myo_KN
import sys
import struct
import time



#Variables Publicas
publish_EMG = [30,30,90]
posiciones = ["Relajado","Puño","Señalar", "Abrir Mano", "Meñique", "Pinza", "insulto",]

try:
    import pygame
    from pygame.locals import *
    HAVE_PYGAME = True
except ImportError:
    HAVE_PYGAME = False




class EMGHandler(object):
    def __init__(self, m):
        self.recording = -1
        self.m = m
        #Creacion del Array
        self.emg = (0,) * 8  

    def __call__(self, emg, moving):
        self.emg = emg
        if self.recording >= 0:
            self.m.cls.store_data(self.recording, emg)
            
            
            

        

if __name__ == '__main__':
    
    if HAVE_PYGAME:
        pygame.init()
        w, h = 900, 500
        scr = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Datos de Protesis SENA")
        font = pygame.font.Font(None, 30)
    

    m = myo_KN.Myo(myo_KN.CLassificador(), sys.argv[1] if len(sys.argv) >= 2 else None)
    
    hnd = EMGHandler(m)
    m.add_emg_handler(hnd)
    
    m.connect()
    last_r = 0
    contador=0
    try:
        while True:
            m.run()
            r = m.history_cnt.most_common(1)[0][0]
            
            if r != last_r:
                #print(r)
                last_r = r
                
            
            if HAVE_PYGAME:
                
                scr.fill((0, 20, 0))#, (800, 0, 800, 320))
                text = "Protesis SENA"
                
                mensaje = font.render(text, 2, (50,255,255))
                scr.blit(mensaje,(15, 5))
                
                for ev in pygame.event.get():
                    if ev.type == QUIT or (ev.type == KEYDOWN and ev.unicode == 'q'):
                        raise KeyboardInterrupt()
                    elif ev.type == KEYDOWN:
                        if K_0 <= ev.key <= K_6:
                            contador +=1
                            print("Grabando posicion " + posiciones[ev.key-K_0] + " dato No: " + str(contador) )                          
                            hnd.recording = ev.key - K_0
                            
                        elif K_KP0 <= ev.key <= K_KP6:
                            hnd.recording = ev.key - K_Kp0
                        elif ev.unicode == 'r':
                            #hnd.cls.entrenar()
                            m.cls.entrenar()
                    elif ev.type == KEYUP:
                        if K_0 <= ev.key <= K_6 or K_KP0 <= ev.key <= K_KP6:
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
                
                
                
    except KeyboardInterrupt:
        pass
        
    finally:
        m.disconnect()
        print()

    if HAVE_PYGAME:
        pygame.quit()


