import socket
skt= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 4500

def original(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))

skt.bind((host, port))

skt.listen()
print('socket is listening...')

cl,addr = skt.accept()
encrypted = cl.recv(2048).decode('utf-8')
print(f'string recieved --> {encrypted}')

key = input('Give the key to decrypt the string, which should be of the same length as the encrypted data -->\n')
decryped = original(encrypted, key)
print(f'the derypted text generated at the server --> {decryped}')
cl.send(decryped.encode('utf-8'))
skt.close()
