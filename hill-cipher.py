keymatrix = [[0]*3 for i in range(3)]
textmatrix = [[0]*3 for i in range(3)]
resultmatrix = [[0]*3 for i in range(3)]
inverse_keymatrix = [[0]*3 for i in range(3)]
decrypted_matrix = [[0]*3 for i in range(3)]

def char_to_num(char):
    return ord(char) - ord('A')

def num_to_char(num):
    return chr(num + ord('A'))

def getKeyMatrix(key):
    index = 0
    for i in range(3):
        for j in range(3):
            keymatrix[i][j] = key[index]
            index += 1
    print('Key Matrix:')
    for row in keymatrix:
        print(row)

def getTextMatrix(text):
    while len(text) < 9:
        text += '_'
    index = 0
    for i in range(3):
        for j in range(3):
            textmatrix[j][i] = text[index]
            index += 1
    print('Text Matrix:')
    for row in textmatrix:
        print(row)

def getResultMatrix(textmatrix, keymatrix):
    for i in range(3):
        for j in range(3):
            for x in range(3):
                resultmatrix[i][j] += char_to_num(keymatrix[i][x]) * char_to_num(textmatrix[x][j])
            resultmatrix[i][j] = num_to_char(resultmatrix[i][j] % 26)  
    print('Result Matrix:')
    for row in resultmatrix:
        print(row)

def decryptText(resultmatrix, keymatrix):
    determinant = 0
    for i in range(3):
        determinant += char_to_num(keymatrix[0][i]) * (char_to_num(keymatrix[1][(i+1)%3]) * char_to_num(keymatrix[2][(i+2)%3]) - char_to_num(keymatrix[1][(i+2)%3]) * char_to_num(keymatrix[2][(i+1)%3]))

    determinant = determinant % 26

    for i in range(3):
        for j in range(3):
            cofactor = (char_to_num(keymatrix[(j+1)%3][(i+1)%3]) * char_to_num(keymatrix[(j+2)%3][(i+2)%3]) - char_to_num(keymatrix[(j+1)%3][(i+2)%3]) * char_to_num(keymatrix[(j+2)%3][(i+1)%3])) % 26
            inverse_keymatrix[i][j] = num_to_char((cofactor * pow(determinant, -1, 26)) % 26)

    for i in range(3):
        for j in range(3):
            for x in range(3):
                decrypted_matrix[i][j] += char_to_num(inverse_keymatrix[i][x]) * char_to_num(resultmatrix[x][j])
            decrypted_matrix[i][j] = num_to_char(decrypted_matrix[i][j] % 26)

    print('Decrypted Matrix:')
    for row in decrypted_matrix:
        print(row)

    decrypted_text = ''
    for i in range(3):
        for j in range(3):
            decrypted_text += decrypted_matrix[j][i]
    decrypted_text = decrypted_text.rstrip('E')
    print('Decrypted Text:', decrypted_text)

key = 'ABDFGYIPQ'
text = (input('Enter Text to Encrypt: ')).upper()
getKeyMatrix(key)
getTextMatrix(text)
getResultMatrix(textmatrix, keymatrix)
decryptText(resultmatrix, keymatrix)