import math
p = int(input('Enter a prime number p: '))
q = int(input('Enter a prime number q: '))

while(p%q==0 or q%p==0):
    print('p and q must be relatively prime!')
    p = int(input('Enter a prime number p: '))
    q = int(input('Enter a prime number q: '))

n = p*q
print('n:', n)
phi = (p-1)*(q-1)
print('phi:', phi)

e = 2
while(math.gcd(e, phi)!=1):
    e += 1

d = 2
while((d*e%phi)!=1):
    d += 1
M = int(input('Enter an integer to encrypt: '))
E = pow(M, e, n)
print('Encrypted Message: ', E)
D = pow(E, d, n)
print('Decrypted Message: ', D)