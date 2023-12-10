import socket

def vigenere_decrypt(text, key):
    result = ''
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - (ord(key[i % key_length].upper()) - 65)) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - 97 - (ord(key[i % key_length].lower()) - 97)) % 26 + 97)
        else:
            result += char
    return result

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Successfully Created!")
port = 2345

s.bind(('localhost', port))
print('Socket binded to %s' % (port))

s.listen(5)
print("Socket is listening")

client_socket, addr = s.accept()
print(f"Accepted connection from {addr}")

encrypted_text = client_socket.recv(1024).decode()
print('Received encrypted value: ', encrypted_text)

key = 'hack'

decrypted_text = vigenere_decrypt(encrypted_text, key)
print('Decrypted value: ', decrypted_text)

client_socket.close()
s.close()
