from tkinter import *
from tkinter import ttk

#Lista de posiciones
tablaPosiciones = []



ventana = Tk()
ventana.title('Sistema Protesis SENNOVA')

frame1 = Frame()
frame1.pack()
frame1.config(width="300", height="100")

frame2 = Frame()
frame2.pack()

frame3 = Frame()
frame3.pack()

def motrarCampos(cantidad):
    for i in range(cantidad):
        
        variableIntrada = StringVar()
        
        #Coloca las etiquetas
        flag1 = "Posicion " + str(i) + ":"
        lbl_pose = Label(frame3,text=flag1)
        lbl_pose.grid(row=i,column=1)
        
        #colocando los entries
        txb_namePosition= Entry(frame3,textvariable=variableIntrada)
        txb_namePosition.grid(row=i,column=2)
        
        #porcada vez que pase el hace un add a  la lista global
        tablaPosiciones.append(variableIntrada)
        
    #Habilita el boton de entrenar
    btn_Next.config(state="disable")
    btn_Entrene.config(state="active")
        
def leerFormulario():
    for i in tablaPosiciones:
        print(i.get())
        
      

titulo = Label(frame1,text="HOLA SENNOVA")
titulo.config(font="courier 70 bold")
titulo.grid(row=1,column=2)

titulo = Label(frame1,text="Digita las posiciones que deseas\nque el sistema tenga")
titulo.config(font="courier 18")
titulo.grid(row=2,column=2)


#miImagen=PhotoImage(file= "/home/pi/Desktop/myo.jpg")
#Label(ventana,image=miImagen).place(x=0,y=0)

numberPositions = IntVar()
numberPositions.set(6)
lbl_numberPositions = Label(frame2,text="Posiciones:")
txb_numberPositions = Entry(frame2,textvariable=numberPositions)

lbl_numberPositions.grid(row=3,column=1)
txb_numberPositions.grid(row=3,column=2, padx=10, pady=10)

btn_Next=Button(frame2, text= "Siguiente",command=lambda:motrarCampos(numberPositions.get()))
btn_Next.grid(row=4,column=1,columnspan = 2)

frame4 = Frame()
frame4.pack()

btn_Entrene=Button(frame4, text= "Entrenar",command=lambda:leerFormulario())
btn_Entrene.grid(row=1,column=1,columnspan = 2)
btn_Entrene.config(state="disable")





ventana.mainloop()

if __name__ == '__main__':
    pass

