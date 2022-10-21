def f(x):
    return x*x + 2*x + 2 

def deriv(f):
    h = 0.001
    def df(x):
        return round((f(x + h) - f(x)) / h, 3)
    return df

print(deriv(f)(3))