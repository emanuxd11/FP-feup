def fact(n):
    if bool(int(n == 1) + int(n == 0)):
        return 1
    return n * fact(n-1)

    #return int(n == 1) * 1 + int(n != 1) * n * fact(n-1)

#print(fact(4))

def C(n, r):
    comb = fact(n) / (fact(r) * fact(n-r))
    return int(comb)