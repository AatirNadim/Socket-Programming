str = input('Give the string to encrypt\n')
key = int(input('Give the key for encryption\n'))

def enc(c, key) :
    if c.islower() :
        return chr((ord(c) - 97 + key)%26 + 97)
    return chr((ord(c) - 65 + key)%26 + 65)

def dec(c, key) :
    if c.islower() :
        return chr((ord(c) - 97 - key + 26)%26 + 97)
    return chr((ord(c) - 65 - key + 26)%26 + 65)

def encrypt(str, key) :
    ls = []
    for c in str :
        ls.append(enc(c, key))
    return ''.join(ls)

def decrypt(str, key) :
    ls = []
    for c in str:
        ls.append(dec(c, key))
    return ''.join(ls)

str1 = encrypt(str, key)
print('The encrypted string -->')
print(str1)
str1 = decrypt(str1, key)
print('Decrypted string -->')
print(str1)
