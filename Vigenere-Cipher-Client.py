import socket

def vigenere_encrypt(text, key):
    result = ''
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + ord(key[i % key_length].upper()) - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - 97 + ord(key[i % key_length].lower()) - 97) % 26 + 97)
        else:
            result += char
    return result

s = socket.socket()
print('Socket Successfully Created!')
port = 2345
s.connect(('127.0.0.1', port))

text = input('Enter text to encrypt: ')
key = 'hack'

encrypted_text = vigenere_encrypt(text, key)
print('Encrypted text: ' + encrypted_text)
s.send(encrypted_text.encode())

s.close()
