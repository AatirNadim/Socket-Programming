import socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
str = input('give the message for encryption\n')
val = input('give the key for encryption\n')
host= '127.0.0.1'
port = 3400
skt.connect((host, port))
print(f'value of val is --> {val}, len is --> {len(val)}, type is --> {type(val)}')
def encrypt(text, key) :
    rail = [['\n' for i in range(len(text))]
                  for j in range(key)]
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))


str1 = encrypt(str, int(val))
print(f'the encryped message from the user is -->\n{str}')
skt.send(str1.encode('utf-8'))
# skt.send(val.encode('utf-8'))
temp = skt.recv(2048).decode('utf-8')
print('decoded value recieved from the server -->')
print(temp)
if temp == str :
    print('values match')
else:
    print('values do not match')
skt.close()