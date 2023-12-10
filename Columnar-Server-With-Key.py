import math
import socket  

s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 23456
s.bind(('127.0.0.1', port))
s.listen(5)
client_socket, addr = s.accept()
def decrypt(text, key):
    result = ''
    key_sorted = sorted(range(len(key)), key = lambda k:key[k])
    rows = math.ceil(len(text)/len(key))

    matrix = [['' for _ in range(len(key))] for _ in range(rows)]
    index = 0
    for j in range(len(key)):
        for i in range(rows):
            matrix[i][key_sorted[j]] = text[index]
            index+=1

    for row in matrix:
        print(row)

    for i in range(rows):
        for j in range(len(key)):
            result += matrix[i][j] 
            
    result = result.replace('_', '')
    return result

key = 'hack'
encrypted_text = client_socket.recv(1024).decode()
decrypted_text = decrypt(encrypted_text, key)
print('decrypted text: ' + decrypted_text)
client_socket.close()
s.close()