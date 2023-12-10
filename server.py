import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
s.bind(('127.0.0.1', port))
s.listen(5)
client_socket, addr = s.accept()

def decryption(plaintext):
    matrix = [['' for i in range(cols)] for i in range (rows)]
    index = 0
    for i in range(cols):
        for j in range(rows):
            matrix[j][i] =  plaintext[index]
            index += 1

    for r in matrix:
        print(r)

    result = ''
    for i in range(rows):
        for j in range(cols):
            result += matrix[i][j]
    
    result = result.replace('_','')
    print('decrypted text: ', result)
    return result

n = client_socket.recv(1024).decode()
rows = int(n[0])
print('encrypted text: ', n.replace(n[0], ''))
cols = int(len(n)/rows)
decrypted_text = decryption(n.replace(n[0], ''))
client_socket.close()
s.close()