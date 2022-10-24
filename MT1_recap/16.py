def deriv(f):
    h = 0.001
    def df(x):
        return round((f(x + h) - f(x)) / h, 3)
    return df

def f(x):
    return x*x + 2*x + 2 
print(deriv(f)(3))

string = "abdef"
string = string[ : len(string) - 1 : ]
print(string)

