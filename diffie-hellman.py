def prime_checker(p):
    for i in range(2,p):
        if p % i == 0:
            return -1
    return 1

def primitive_finder(p):
    primitive_root = -1
    for g in range(2,p):
        L = [pow(g, i, p) for i in range(1,p)]
        if (len(set(L))==p-1):
            primitive_root = g
            break
    return primitive_root

p = int(input('Enter p: '))
print(prime_checker(p))
a = primitive_finder(p)
print('Primitive Root: ', a)
Xa = int(input('Enter Private key of user 1: '))
Xb = int(input('Enter Private key of user 2: '))

while (Xa>p or Xb>p):
    print(f"Private Key Of Both The Users Should Be Less Than {p}!")
    Xa = int(input('Enter Private key of user 1: '))
    Xb = int(input('Enter Private key of user 2: '))   

Ya = pow(a, Xa, p)
Yb = pow(a, Xb, p)
print(f'Public Keys are {Ya} and {Yb}')

Ka = pow(Yb, Xa, p)
Kb = pow(Ya, Xb, p)
print(f'Keys are {Ka} and {Kb}')