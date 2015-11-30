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
nombre = receiver[0]
IP = receiver[1].split(':')[0]
SIPport = int(receiver[1].split(':')[1])
print(nombre + "nombre")
print(receiver )
print (RECEPTOR + "RECEPTOR")
print (SIPport )
print (IP)
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP, SIPport))
ENVIAR = METHOD + ' sip:' + nombre + '@' + 'SIP/2.0'
print("Enviando: " + ENVIAR)
my_socket.send(bytes(ENVIAR, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)
print('Recibido -- ', data.decode('utf-8'))
lista = data.decode('utf8').split('\r\n\r\n')
print(lista)

if 'SIP/2.0 100 Trying' in lista and 'SIP/2.0 180 Ring' in lista and 'SIP/2.0 200 OK' in lista:
    ACK = ('ACK' + ' ' + 'sip:' + nombre + '@' + IP + ' ' + 'SIP/2.0')
    my_socket.send(bytes(ACK, 'utf-8') + b'\r\n')
    print("Enviando: " + ACK)
    data = my_socket.recv(1024)


print("Terminando socket...")
# Cerramos todo
my_socket.close()
print("Fin.")
