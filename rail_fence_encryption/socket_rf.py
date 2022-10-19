import socket 
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 3400
skt.bind((host, port))
print(f'server is listening on port {port}')
skt.listen()


def decrypt(cipher ,key) :
    rail = [['\n' for i in range(len(cipher))]
                  for j in range(key)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))
    pass
while True:
    cl, addr = skt.accept()
    print(f'connection established with {cl}')
    str = cl.recv(2048).decode('utf-8')
    print('encryted message from the client -->')
    print(str)
    val = int(input('give the key for decryption\n'))
    # val= int(val)
    str = decrypt(str, val)
    print('decoded message recieved from the client -->')
    print(str)
    # print('')