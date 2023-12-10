import socket

s = socket.socket()
print('Socket Successfully Created!')
port = 2345
s.connect(('127.0.0.1', port))
def encrypt(text, shift):
    result = ''
    for char in text:
        if char.isupper():
            result += chr(((ord(char) - 65 +shift) % 26)+65)
        elif char.islower():
            result += chr(((ord(char) - 97 +shift) % 26)+97)
        else:
            result += char
    return result
text = input('enter text to encrypt: ')
shift = 3
n = encrypt(text, shift)
s.send(n.encode())
s.close()