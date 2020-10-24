from math import gcd

def is_prime(num):
    if num <= 2:
        return num == 2

    if num % 2 == 0:
        return False

    for divisor in range(3, int(num ** 0.5) + 1, 2):
        if num % divisor == 0:
            return False

    return True
def is_carmichael(n):

    # Carmichael number is an odd composite number
    if n <= 2 or n % 2 == 0 or is_prime(n):
        return False

    for a in range(3, n, 2):
        if gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False

    return True

def carmichaelNumbers(max):
    print("Carmichael numbers less than 10000")
    for num in range(max):
        if is_carmichael(num):

            print(num)


carmichaelNumbers(10000)