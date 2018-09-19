#! / usr / bin / python

import  os ,  sys 
import  tty 
desde  seleccionar  importar  seleccionar

clase  NotTTYException ( Exception ):  pase

clase  TerminalFile : 
    def  __init__ ( self , infile ): 
        if  no  infile . isatty (): 
            sube  NotTTYException () 
        self . file = infile

        #prepare para getch 
        self . save_attr = tty . tcgetattr ( auto . archivo ) 
        newAttr = auto . save_attr [:] 
        newattr [ 3 ]  & =  ~ tty . ECHO  &  ~ tty . ICANON 
        TTY . tcsetattr ( auto . archivo ,  TTY . TCSANOW ,  newAttr )

    def  __del__ ( self ): 
        #restoring stdin 
        import  tty   #required this import here 
        tty . tcsetattr ( auto . archivo ,  TTY . TCSADRAIN ,  sí . save_attr )

    def  getch ( auto ): 
        si  seleccione ([ auto . archivo ], [], [], 0 ) [ 0 ]: 
            c = auto . archivo . leer ( 1 ) 
        else : 
            c = '' 
        return  c

si  __name__ == "__main__" : 
    s = TerminalFile ( sys . stdin ) 
    print  "Presione q para salir ..." 
    i = 0 
    mientras  s . getch () ! = "q" : 
        sys . stdout . write ( " % 08d \ r " % i ) 
        i + = 1 
    print  "- END -"