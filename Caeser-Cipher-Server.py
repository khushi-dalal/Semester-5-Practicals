import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Successfully Created!")
port = 2345

s.bind(('localhost', port))
print('Socket binded to %s' % (port))

s.listen(5)
print("Socket is listening")

client_socket, addr = s.accept()
print(f"Accepted connection from {addr}")

def decrypt(text, shift):
    result = ''
    for char in text:
        if char.isupper():
            result += chr(((ord(char) - 65 +shift) % 26)+65)
        elif char.islower():
            result += chr(((ord(char) - 97 +shift) % 26)+97)
        else:
            result += char
    return result

text = client_socket.recv(1024).decode()
print('recieved value: ', text)
shift = 23
print('decrypted value: ', decrypt(text, shift))
client_socket.close()
s.close()