#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os

try:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    fichero_audio = sys.argv[3]
except IndexError:
    print("Usage: python server.py IP port audio_file")


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    METHOD = ["INVITE", "BYE", "ACK"]

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            linea = line.decode('utf_8')
            Method = linea.split()[0]
            print("El cliente nos manda " + line.decode('utf-8'))
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

            if Method == 'INVITE':
                print("El cliente nos manda " + line.decode('utf-8'))
                self.wfile.write(b"SIP/2.0 100 Trying\r\n\r\n" + b"SIP/2.0 180 Ring\r\n\r\n" + b"SIP/2.0 200 OK\r\n\r\n")

            elif Method == 'ACK':
                print("El cliente nos manda " + line.decode('utf-8'))
                aEjecutar = './mp32rtp -i 127.0.0.1 -p 23032 <' + fichero_audio
                print("Vamos a ejecutar " + aEjecutar)
                os.system(aEjecutar)

            elif Method == 'BYE':
                print("El cliente nos manda " + line.decode('utf-8'))
                self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

            elif Method not in METHOD:
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed\r\n\r\n")
            else:
                self.wfile.write(b"SIP/2.0 400 Bad Request\r\n\r\n")

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer((IP, PORT), EchoHandler)
    print("Listening...")
    serv.serve_forever()
