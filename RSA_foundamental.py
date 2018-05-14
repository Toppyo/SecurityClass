import math

def cmpex(a, b):
    return (a, b) if a>b else (b, a)

def modtool(a, b):
    a, b = cmpex(a, b)
    return int(a/b), a%b

def gcd_base(a, b):
    quotient_list = []
    a, b = cmpex(a, b)
    while a%b!=0:
        quotient_list.append(int(a/b))
        a, b = b, a%b
    return b, quotient_list

def gcd(a, b):
    a, b = cmpex(a, b)
    GCD, ql = gcd_base(a, b)
    t, s = findParam(a, b, ql, 1)
    return GCD, t, s

def findParam(a, b, list, n):
    if n==len(list)+1:
        return 1, 0
    elif n==len(list)+2:
        return 0, 1
    else:
        previous_T, previous_S = findParam(a, b, list, n+1)
        previous_previous_T, previous_previous_S = findParam(a, b, list, n+2)
        return previous_previous_T-previous_T*list[-n], previous_previous_S-previous_S*list[-n]

def eulerTotientF(n):
    result = 1
    dividerDict = {}
    startPoint = 2
    eulerTotientF_base(n, startPoint, dividerDict)
    for key in dividerDict.keys():
        result *= (pow(key, dividerDict[key]) - pow(key, dividerDict[key]-1))
    return result

def eulerTotientF_base(n, startPoint, dividerDict):
    i = startPoint
    isPrime = True
    while i < math.sqrt(n):
        count = 0
        while n%i == 0:
            count += 1
            n /= i
        if(count>0):
            isPrime = False
            dividerDict[i] = count
            eulerTotientF_base(int(n), i+1, dividerDict)
            break
        i += 1
    if isPrime:
        dividerDict[n] = 1

def Q1(a, b):
    GCD, t, s = gcd(a, b)
    print("GCD is: " + str(GCD))
    print("Paraneter s is: " + str(s))
    print("Paraneter t is: " + str(t))

def Q2(a, m):
    GCD, t, s = gcd(a, m)
    print("The inverse of a modulo m is: " + (str(t) if t>0 else str(t+m)))

def Q3(n):
    print("The value of Φ(" + str(n)+") is: " + str(eulerTotientF(n)))

def main():
    print("Question 1:")
    Q1(198, 243)
    Q1(1819, 3587)
    print("Question 2:")
    Q2(7, 26)
    Q2(19, 999)
    print("Question 3:")
    Q3(33)
    Q3(56)

if __name__ == "__main__":
    main()