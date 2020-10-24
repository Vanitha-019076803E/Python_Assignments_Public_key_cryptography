# Addition implementation algorithm

B = 10

def addition(a, b):
    carry = 0
    res = []
    for i in range(0, len(b)):
        tmp = int(a[len(a) - 1 - i]) + int(b[len(b) - 1 - i]) + carry
        carry = int(tmp / B)
        res.append(tmp % B)
    for i in range(len(b), len(a)):
        tmp = int(a[len(a) - 1 - i]) + carry
        carry = int(tmp / B)
        res.append(tmp % B)

    res.append(carry)
    result = ""
    for i in range(len(res) - 1, -1, -1):
        result = result + str(res[i])
    return result


if __name__ == '__main__':
    a = "99999999999999999"
    b = "1000000000"
    addition_result = addition(a, b)
    print("The addition of big integers \n"+a+" + "+b+ " = " +addition_result)
