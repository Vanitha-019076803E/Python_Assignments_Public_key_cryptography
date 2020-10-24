from vanitha.homework2.Addition import addition

#Fibanocci series implementation

arr = ["1", "1"]


def fibanocci(n):

    if n < 0:
        print("Enter a positive integer")
    elif n < len(arr):
        return arr[n]
    else:
        tmp = addition(fibanocci(n - 1), fibanocci(n - 2))
        arr.append(tmp)
        return tmp

"""
I am getting n value in run time and for n = 100 I am getting the same value which is given in the question 573147844013817084101
for n = 101 the fibanocci value is 927372692193078999176
"""

if __name__ == '__main__':

    number = int(input("Enter the value of n = "))
    print(fibanocci(number).lstrip("0"))
    print("\nFor n = 101 the fibanocci series is "+str(fibanocci(101).lstrip("0")))