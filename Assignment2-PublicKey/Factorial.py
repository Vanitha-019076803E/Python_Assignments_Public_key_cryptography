from vanitha.homework2.Multiplication import mul


# Implementation of factorial

def factorial(num):
    if num < 0:
        return "Factorial cannot be found for negative numbers"
    elif num == 0:
        return "1"
    elif num == 1:
        return str(num)
    else:
        return mul(str(num).lstrip("0"), factorial(num-1).lstrip("0"))



"""
I checked the factorial for 30 and got the same value(265252859812191058636308480000000) 
which is given in the question paper and also the factorial of 40 is 815915283247897734345611269596115894272000000000

"""

if __name__ == '__main__':
    num = int(input("Enter a Number: "))
    print(factorial(num))
    print("\nThe factorial of 40 is ")
    print(factorial(40))
