def encrypt(text, a, b):
    result = ''
    for char in text:
        encrypted_char = chr(((ord(char) - 97) * a + b) % 26 + 97)
        result += encrypted_char
    return result

def a_inv(a):
    x = 0
    while(((a * x) % 26) != 1):
        x+=1
    print('a inverse: ', a)
    return x

def decrypt(text, a, b):
    result = ''
    x = a_inv(a)
    for char in text:
        decrypted_char = chr(((ord(char) - 97 - b) * x) % 26 + 97)
        result += decrypted_char
    return result

a = 3
b = 5
text = input('Enter text: ')
encrypted_text = encrypt(text, a, b)
print("Encrypted text:", encrypted_text)
decrypted_text = decrypt(encrypted_text, a, b)
print("Decrypted text:", decrypted_text)