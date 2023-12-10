import random
 
# Function to generate a super-increasing sequence for the public key
def generate_super_increasing_sequence(n):
    sequence = [random.randint(1, 100)]
    while len(sequence) < n:
        next_element = sum(sequence) + random.randint(1, 10)
        sequence.append(next_element)
    return sequence
 
# Function to generate the private key from the public key
def generate_private_key(public_key, q, r):
    private_key = [(r * element) % q for element in public_key]
    return private_key
 
# Function to encrypt the plaintext using the public key
def knapsack_encrypt(plaintext, public_key):
    encrypted_message = sum(public_key[i] for i in range(len(plaintext)) if plaintext[i] == '1')
    return encrypted_message
 
# Example usage
if __name__ == "__main__":
    n = 8  # Number of elements in the super-increasing sequence
    q = 103  # Modulus (should be greater than the sum of the super-increasing sequence)
    r = 3  # Multiplier for generating private key
 
    # Generate the public key and private key
    public_key = generate_super_increasing_sequence(n)
    private_key = generate_private_key(public_key, q, r)
 
    plaintext = input('Enter 8-bit Binary Message to Encrypt: ')
    ciphertext = knapsack_encrypt(plaintext, public_key)
 
    print("Original Message:", plaintext)
    print("Private Key:", private_key)
    print("Public Key:", public_key)
    print("Encrypted Ciphertext:", ciphertext)