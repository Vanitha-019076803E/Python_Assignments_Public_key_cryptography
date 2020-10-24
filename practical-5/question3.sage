from sage.all import *

"""
******** How could such error be detected ????? *************
A powerful countermeasure against the Bellcore attack(to detect the error) is to raise the signature to the power e and to compare the
result with the input message m. If the signature is faulty the comparison will detect it. A possible obstacle is that in
practice e is not always available to the signer function.
"""

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
    print("\nIs replaced value of fault_p and original p equal????:::::: "+str(p==fault_p))
    print("\nfault_p = "+str(fault_p))
    fault_sp = m.powermod(d.mod(fault_p - 1), fault_p)
    sq = m.powermod(d.mod(q - 1), q)
    fault_s= CRT(fault_sp, sq, p, q)
    print("\nSignature(s) using CRT with faulty private key = " +str(fault_s))
    return fault_s,Nn,e

"""
Error detection using m = s ^ e mod N........
"""
def detectingError(fault_s,Nn,e):
    faulty_message = fault_s.powermod(e,Nn)
    return faulty_message


if __name__ == "__main__":
    message = 1234556778
    fault_s,Nn,e = fault_in_signatureGen(message)
    faulty_message =detectingError(fault_s,Nn,e)
    print("\nOriginal message = "+str(message),"\nFaulty message = "+str(faulty_message))
    print("\nIs original message equal to faulty_message???? = "+str(message==faulty_message))
    if message != faulty_message:
        print("\nError Detected!!!!!!!!!!!!!!!!!\n")

