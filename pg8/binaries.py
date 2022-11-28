def fib(lol):
    return [int, lambda *_ : fib(lol - 1) + fib(lol - 2)][lol >= 2](lol)

def no_consecutives1(k):
    return fib(k + 2)

print(no_consecutives1(7))