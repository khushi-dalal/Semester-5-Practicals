plaintext = input('enter text to encrypt: ')
def s_box(plaintext):
    shift = 3
    result = ''
    for i in range(len(plaintext)):
        if plaintext[i].isupper():
            result += chr((ord(plaintext[i])-shift-ord('A'))%26+ord('A'))
        elif plaintext[i].islower():
            result += chr((ord(plaintext[i])-shift-ord('a'))%26+ord('a'))
        else:
            result+=plaintext[i]
    return result

def inverse_s_box(plaintext):
    shift = 3
    result = ''
    for i in range(len(plaintext)):
        if plaintext[i].isupper():
            result += chr((ord(plaintext[i])+shift-ord('A'))%26+ord('A'))
        elif plaintext[i].islower():
            result += chr((ord(plaintext[i])+shift-ord('a'))%26+ord('a'))
        else:
            result+=plaintext[i]
    return result

def p_box(text):
    result = ''
    permutation = [2, 0, 3, 1, 4]
    result = [text[i] for i in permutation]
    return ''.join(result)

def inverse_p_box(text):
    result = [''] * len(text)
    permutation = [2, 0, 3, 1, 4]
    for i in range(len(permutation)):
        result[permutation[i]] = text[i]
    return ''.join(result)

after_s_box = s_box(plaintext)
print('after s-box: ', after_s_box)
after_p_box = p_box(after_s_box)
print('after p-box: ', after_p_box)
after_inverse_p_box = inverse_p_box(after_p_box)
print('after reverse p-box: ', after_inverse_p_box)
after_reverse_s_box = inverse_s_box(after_inverse_p_box)
print('after reverse s-box: ', after_reverse_s_box)