import sys
import struct
import time
import os


from armBand import myo_KN

try:
    import pygame
    from pygame.locals import *
    HAVE_PYGAME = True
except ImportError:
    HAVE_PYGAME = False


#m.add_emg_handler()

##m = Myo(CLassificador(), sys.argv[1] if len(sys.argv) >= 2 else None)

print(os.getcwd())