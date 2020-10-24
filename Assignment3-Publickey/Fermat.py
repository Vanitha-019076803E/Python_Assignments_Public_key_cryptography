import random as rand
from sage.all import *

# Security parameter
t = 10

"""
(i)Fermat's primality test
"""


def primality_test(n):
    for i in range(0, t):
        a = rand.randint(2, n - 2)
        r = (a ** (n - 1)) % n
        if r != 1:
            return "'n'is composite"
        else:
            return "n is prime"

"""
(ii)function to generate random k-bit prime numbers using SAGE
"""


def genearate_random_prime(k):

    for i in range(0, (2**k)-1):
        n = random_prime((2 ** k) - 1, false, 2 ** (k - 1))
        res = primality_test(n)
        if res == "n is prime":
            return n


if __name__ == "__main__":
    n = int(input("\nEnter a value of 'n' to check whether it is prime = "))
    print(primality_test(n))
    k = int(input("\nEnter k bits to generate random prime numbers = "))
    print("Prime number : "+str(genearate_random_prime(k)))