
# Modular exponentiation algorithm implementation


def expmod(a, b, n):
    c = 1

    for i in range(len(b)-1, -1, -1):
        c = (c * c) % n
        if b[len(b)-1-i] == "1":
            c = (c * a) % n
    return c


if __name__ == '__main__':
    a = 2342
    b = 6762
    n = 9343
    print("\na = "+str(a), "b = "+str(b), "c = "+str(n))
    b_bin = bin(b)[2:]
    modular_exp = expmod(a, b_bin, n)
    print("\n"+str(a)+" ^ "+str(b)+" mod "+str(n)+" ≡ "+str(modular_exp))
