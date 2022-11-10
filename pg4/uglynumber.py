def rec_factor(x, y):
    d = {True : lambda x, y : x, False : lambda a, b : rec_factor(a / b, b)}
    return d[x % y != 0](x, y)

def ugly(n):
    return True * (rec_factor(rec_factor(rec_factor(n, 2), 3), 5) == 1)

print(ugly(8))
