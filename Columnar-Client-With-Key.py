import math
import socket  

s =  socket.socket()
port = 23456
s.connect(('127.0.0.1', port))

def encrypt(text, key):
    result = ''
    key_sorted = sorted(range(len(key)), key = lambda k:key[k])
    rows = math.ceil(len(text)/len(key))
    while len(text)%len(key) != 0:
        text+='_'
    matrix = [['' for _ in range(len(key))] for _ in range(rows)]
    index = 0
    for i in range(rows):
        for j in range(len(key)):
            matrix[i][j] = text[index]
            index+=1
    for row in matrix:
        print(row)
    for j in range(len(key)):
        for i in range(rows):
            result += matrix[i][key_sorted[j]]
    return result

text = input('enter text: ')
key = 'hack'
encrypted_text = encrypt(text, key)
print('encrypted text: ' + encrypted_text)

s.send(encrypted_text.encode())
s.close()