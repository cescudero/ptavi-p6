#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
#SERVER = 'localhost'
#PORT = 6001

# Contenido que vamos a enviar
#LINE = '¡Hola mundo!'
try:
    METHOD = sys.argv[1]
    RECEPTOR = sys.argv[2]
except IndexError:
    print("Usage: python client.py method receiver@IP:SIPpor")

receiver = RECEPTOR.split('@')
SERVER = receiver[1].split(':')[0]
SIPport = receiver[1].split(':')[1]
print(SIPport)
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, int(SIPport)))

print("Enviando: " + METHOD + ' ' + RECEPTOR)
my_socket.send(bytes(METHOD, 'utf-8') + bytes(RECEPTOR, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
