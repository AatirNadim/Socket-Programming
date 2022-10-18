import socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port= 3400
skt.connect((host, port))
while True:
    str = skt.recv(2048)
    temp = str.decode('utf-8')
    print(f'message recieved from the server --> {temp}')
    skt.send('now this is a message from me'.encode('utf-8'))

