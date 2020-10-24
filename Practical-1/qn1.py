
# Euclid's Algorithm
def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


a = int(input("Enter the value of 'a' :" ))
b = int(input("Enter the value of 'b' :" ))
print("gcd(", a, ",", b, ") = ", gcd(a, b))
