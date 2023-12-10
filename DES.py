plaintext = input('Enter 8-bit binary text to encrypt: ')
key = input('Enter 4-bit binary key: ')

def initial_permutation(input_block):
    # Initial Permutation
    permutation_table = [1, 5, 2, 0, 3, 7, 4, 6]
    permuted_block = [input_block[i] for i in permutation_table]
    return permuted_block

def xor_operation(text1, text2):
    """Perform the XOR operation on two binary strings."""
    return ''.join(str(int(bit1)^int(bit2)) for bit1, bit2 in zip(text1, text2))
    
def swapper(right_half, left_half):
    result = ''
    result = result + right_half + left_half
    return result

def DES_Round(plaintext, key):
    left_half = plaintext[:4]
    print('left half:', left_half)
    right_half = plaintext[4:]
    print('right half:', right_half)
    new_right_half = xor_operation(right_half, key)
    print('new right half:', new_right_half)

    new_left_half = xor_operation(new_right_half, left_half)
    print('new left half:', new_left_half)
    print('final output: ', swapper(new_right_half, new_left_half))

plaintext = format(int(plaintext, 2), '08b')  # Convert to 8-bit binary string
key = format(int(key, 2), '04b')  # Convert to 4-bit binary string
plaintext = initial_permutation(plaintext)
print('permuted text: ', plaintext)
DES_Round(plaintext, key)
