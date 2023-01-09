from functools import reduce

def evaluate(a, x):
    return reduce(lambda x, y : x+y, map(lambda enum : enum[1]*x**enum[0], enumerate(a)))

print(evaluate([1, 2, 4], 5))