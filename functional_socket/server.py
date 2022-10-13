import socket
import sys
import re
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4500
host = '127.0.0.1'

s.bind((host, port))
s.listen()
while True :
    c, addr = s.accept()
    print(f'connection established with {c}, at the address {addr}')
    message = c.recv(1024).decode('utf-8')
    print(f'the message from the client is --> \n{message}')
    str = 'default '
    if re.match(r'^[0-9]+$', message):
        str = str + 'number '
    if re.match(r'^[a-zA-Z]+$', message) :
        str = str + 'string '
    if re.match(r'^[0-9]+\.[0-9]+$',message) :
        str = str + 'float '
    if re.match(r'^[a-zA-Z]+[0-9]+$',message) :
        str= str + 'alphanumeric '
    c.send(str.encode('utf-8'))
    c.close()
    # break

