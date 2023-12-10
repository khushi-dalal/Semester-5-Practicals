import socket

s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))

plaintext = input('Enter Text: ')
rows = int(input('Enter Rows: '))

while (len(plaintext) % rows) != 0:
    plaintext += '_'
cols = int(len(plaintext)/rows)

def encryption(plaintext):
    matrix = [['' for i in range(cols)] for i in range (rows)]
    index = 0
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] =  plaintext[index]
            index += 1

    for r in matrix:
        print(r)

    result = ''
    for i in range(cols):
        for j in range(rows):
            result += matrix[j][i]

    print('result: ', result)
    return result

encrypted_text = str(rows) + encryption(plaintext) 
s.send(encrypted_text.encode())
s.close()