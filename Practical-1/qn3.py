# Iterative Python 3 program to find
# modular inverse using extended
# Euclid algorithm

# Returns modulo inverse of a with
# respect to m using extended Euclid
# Algorithm Assumption: a and m are
# coprimes, i.e., gcd(a, m) = 1
def inverse(a, m) :
	m0 = m
	y = 0
	x = 1

	if (m == 1) :
		return 0

	while (a > 1) :

		# q is quotient
		q = a // m

		t = m

		# m is remainder now, process
		# same as Euclid's algo
		m = a % m
		a = t
		t = y

		# Update x and y
		y = x - q * y
		x = t


	# Make x positive
	if (x < 0) :
		x = x + m0

	return x


# Driver program to test above function



def gcd(a, b):
    # Everything divides 0
    if (a == 0 or b == 0): return 0

    # base case
    if (a == b): return a

    # a is greater
    if (a > b):
        return gcd(a - b, b)

    return gcd(a, b - a)


# Function to check and print if
# two numbers are co-prime or not
def coprime(a, b):
    if (gcd(a, b) == 1):
        print(inverse(a, m))
    else:
        print("%d has no inverse modulo %d" % (a, m))

a = int(input("Enter the value of 'a' : " ))
m = int(input("Enter the value of 'm' : " ))
coprime(a, m)