def parity_drop(original_key):
    result = ''
    for i in [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]:
        result += original_key[i]
    return result

def left_circular_shift(text):
    result = ''
    result += text[1:] + text[:1]
    return result

def compression_box(text):
    result = ''
    p_box = [4, 3, 8, 9, 1, 2, 0, 7]
    for i in p_box:
        result += text[i]
    return result
original_key = input('enter 12-bit key: ')

after_parity_drop = parity_drop(original_key)
print('After Parity Drop: ', after_parity_drop)

left_half = after_parity_drop[:5]
print('left half: ', left_half)
right_half = after_parity_drop[5:]
print('right half: ', right_half)

new_right_half = left_circular_shift(right_half)
new_left_half = left_circular_shift(left_half)

print('new left half: ', new_left_half)
print('new right half: ', new_right_half)

after_left_shift = new_left_half +  new_right_half
key = compression_box(after_left_shift)
print('Round 1 key: ', key)