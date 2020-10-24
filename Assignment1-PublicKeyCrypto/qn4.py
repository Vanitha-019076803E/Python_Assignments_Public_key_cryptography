
# Chinese Remainder


# k is size of num[] and rem[]. Returns the smallest number x such that:
# x % num[0] = rem[0],
# x % num[1] = rem[1],

# x % num[k-2] = rem[k-1]
# Assumption: Numbers in num[] are pairwise coprime (gcd for every pair is 1)
def restechinois(num, rem, k):
    x = 1  # Initialize result

    # As per the Chinise remainder theorem, this loop will always break.
    while (True):

        # Check if remainder of x % num[j] is rem[j] or not (for all j from 0 to k-1)
        j = 0
        while (j < k):
            if (x % num[j] != rem[j]):
                break
            j += 1

        # If all remainders matched, we found x
        if (j == k):
            return x

        # Else try next numner
        x += 1

# Driver Code

# m = int(input("Enter the value of 'm' : "))
# i = 0
# num = []
# rem = []
# while i < m:
#     num[i] = int(input("Enter values of n1, n2,.... : "))
#     i += 1
#
# while i < m:
#     rem[i] = int(input("Enter values of a1,a2,.... : "))
#     i += 1


num = [5, 7]  # values of n1,n2,.....
rem = [4, 3]  # values of a1,a2,.....
m = len(num)
print("z is", restechinois(num, rem, m))

