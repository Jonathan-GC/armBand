'''
import os, sys

from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

if __name__=="__main__":
    
    while True:
        # pressing a key
        k.press_key('H')
        # which you then follow with a release of the key
        k.release_key('H')
        # or you can 'tap' a key which does both
        k.tap_key('e')
        # note that that tap_key does support a way of repeating keystrokes with a interval time between each
        k.tap_key('l',n=2,intervall=5) 
        # and you can send a string if needed too
        k.type_string('o World!')
'''
#!/usr/bin/python

import sys

x = 'si'

while x=='si':
    tecla = sys.stdin.read(1)
    if tecla != 's':
        print("presiono: ", tecla)
    else:
        x='no'
        print("presiono: ", tecla, " chao...")
        

