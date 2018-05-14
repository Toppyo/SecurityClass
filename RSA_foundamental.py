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
    s, t = findParam(a, b, ql, 1)
    return GCD, s, t

def findParam(a, b, list, n):
    if n==len(list)+1:
        return 1, 0
    elif n==len(list)+2:
        return 0, 1
    else:
        previous_S, previous_T = findParam(a, b, list, n+1)
        previous_previous_S, previous_previous_T = findParam(a, b, list, n+2)
        return previous_previous_S-previous_S*list[-n], previous_previous_T-previous_T*list[-n]

# print(cmpex(2, 5))
# print(gcd_base(57888, 9234))
# print(modtool(64000, 9234))
print(gcd(19, 999))