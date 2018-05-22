import security.RSA_foundamental as tools

def getPrvK(p, q, e, n=None):
    if n == None:
        n = p*q
    phi = tools.eulerTotientF(n)
    GCD, t, s = tools.gcd(e, phi)
    return t if t>0 else (t+phi)

def RSAen(p, q, e, M):
    return pow(M, e)%(p*q)

def RSAde(p, q, e, E):
    d = getPrvK(p, q, e)
    return pow(E, d)%(p*q)

def Q1(p, q, e, M):
    Y = RSAen(p, q, e, M)
    X = RSAde(p, q, e, Y)
    print("Encryption result is: " + str(Y))
    print("Decryption result is: " + str(X))

def Q2(C, e, n):
    d = getPrvK(0, 0, e, n)
    print("Decryption result is: " + str(pow(C, d)%n))

def main():
    print("The answer to the 1st question is: ")
    Q1(5, 11, 3, 9)
    Q1(11, 13, 11, 7)
    print("\nThe answer to the 2nd question is: ")
    Q2(10, 5, 35)

if __name__ == '__main__':
    main()