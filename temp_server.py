import socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 3400
skt.bind((host, port))

skt.listen()
cl, cl_adr = skt.accept()
def func(str) :
    pass
while(True) :
    cl.send('this is a temp message'.encode('utf-8'))
    str = cl.recv(2048) #encoded format
    temp = str.decode('utf-8')
    print(f'message from the client is --> {temp}')
    # cl.send(func(str)encode)
skt.close()
