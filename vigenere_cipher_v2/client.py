import socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port= 4500

str= input('Give the value to be encrypted --> \n')
temp = input('Give the value to encrypt --> \n')

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def encrypt(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

key = generateKey(str, temp)
encrypted = encrypt(str, key)

print(f'generated key --> {key}')
print(f'encrypted string --> {encrypted}')

skt.connect((host, port))
skt.send(encrypted.encode('utf-8'))

str2 = skt.recv(2048).decode('utf-8')
print(f'the decrypted string recieved from the server --> {str2}')
if(str2 == str) :
    print('Server decrypted the message correctly')
else :
    print('Server did not decrypt the message correctly')



