from sage.all import *

def keyGen(n=256):
    "Generates an RSA key"
    while True:
        p = random_prime(2 ^ (n // 2));
        q = random_prime(2 ^ (n // 2));
        e = 3
        if gcd(e, (p - 1) * (q - 1)) == 1: break
    d = inverse_mod(e, (p - 1) * (q - 1))
    Nn = p * q
    print("\np = ", p, "\nq = ", q)
    print("\nN = ", Nn)
    print("Size of N:", Nn.nbits())
    return Nn, p, q, e, d

"""
Inducing fault in p....so produced sp will have fault.....from known fault sp and singature s one can find the original private key p
"""
def fault_in_signatureGen(m):
    Nn, p, q, e, d =keyGen()
    fault_p = p+1
    print("\nIs replaced value of fault_p and original p equal????::::::"+str(p==fault_p))
    print("\nfault_p = "+str(fault_p))
    fault_sp = m.powermod(d.mod(fault_p - 1), fault_p)
    sq = m.powermod(d.mod(q - 1), q)
    fault_s= CRT(fault_sp, sq, p, q)
    print("\nSignature(s) using CRT with faulty private key = " +str(fault_s))
    return fault_s,fault_sp,Nn

"""
***********Explanation of how to recover factorization of N*******************
Suppose either sp or sq is computed with a fault. Assuming that the resulting faulty signature sp' or sq' together with the
correct signature s are known to the attacker. Then he can retrieve the private key by computing
      gcd(s – s', N)
for the publicly known RSA modulus N.
The reason for this behaviour is that p and q are used in the CRT recombination in an asymmetric way.
"""
def recoverFactorizationOf_N(fault_s,fault_sp,Nn):
    p = gcd(fault_s-fault_sp,Nn)
    return p


if __name__ == "__main__":
    message = 1234556778
    fault_s,fault_sp,Nn = fault_in_signatureGen(message)
    p =recoverFactorizationOf_N(fault_s,fault_sp,Nn)
    print("\nRecoverved 'p'::::::factor of N = "+str(p)+"\n")

