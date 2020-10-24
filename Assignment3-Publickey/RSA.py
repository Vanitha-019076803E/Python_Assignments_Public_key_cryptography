import random as rand
from sage.all import *


'''
From Homework-1
Euclid's algorithm for determining the greatest common divisor
'''


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''
From Homework-1
Euclid's extended algorithm to find the multiplicative inverse of two numbers
'''


def multiplicative_inverse(e, d):
    m0 = d
    y = 0
    x = 1
    if (d == 1):
        return 0
    while (e > 1):
        # q is quotient
        q = e // d

        t = d

        d = e % d
        e = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + m0

    return x

'''
generating two prime numbers
'''


def generate_two_primes(k):
    k = k / 2
    p = 0
    q = 0

    while True:
        p = random_prime((2 ** k) - 1, false, 2 ** (k - 1))
        if int(p).bit_length() == k:
            break
    while True:
        q = random_prime((2 ** k) - 1, false, 2 ** (k - 1))
        if int(q).bit_length() == k:
            break
    return p, q


def keypair_generation(p, q):

    n = p * q

    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are co prime
    e = rand.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are co prime
    g = gcd(e, phi)
    while g != 1:
        e = rand.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return e, n, d


"""
encrypting message with public keys e 
"""


def encrypt(message, e, n):
    return (message ** e) % n

"""
decrypting cipher text with private key d
"""


def decrypt(cipher_text, d, n):
    return (cipher_text ** d) % n


if __name__ == '__main__':
    message = 1111

    print("\n**** Generating two prime numbers ****")
    k = int(input("Enter k bits = "))
    p,q = generate_two_primes(k)
    print("Prime numbers p and q : ",str(p)+" and "+str(q))

    print("\n**** Generating your public/private keypairs now ****")
    e,n,d = keypair_generation(p, q)
    print("public keys e and n : ", str(e)+" and "+str(n)+ "\nprivate key d : ", d)

    print("\n**** Encryption ****")
    cipher_text=encrypt(message,e,n)
    print("MESSAGE : "+str(message))
    print("CIPHER TEXT : "+str(cipher_text))

    print("\n**** Decryption ****")
    recovered_message = decrypt(cipher_text, d, n)
    print("RECOVERED MESSAGE : " + str(recovered_message))

    print("\n**** Checking whether decryption works ****")
    msg_to_encrypt=11
    print("Encryption")
    print("plain text : ",str(msg_to_encrypt))
    cipher_text = encrypt(msg_to_encrypt, e, n)
    print("cipher text : ", cipher_text)

    print("\nDecryption")
    recovered_message = decrypt(cipher_text, d, n)
    print("Recovered plain text : ", recovered_message)

    if msg_to_encrypt == recovered_message:
        print ("\nDECRYPTION WORKS :) ")


















