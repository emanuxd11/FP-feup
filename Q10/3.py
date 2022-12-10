import itertools

def pythagoreans(a, b):
    return ((x, y, z) 
        for x in range(a, b)
        for y in range(x, b)
        for z in range(y, b)
        if x**2 + y**2 == z**2)

print(list(itertools.islice(pythagoreans(1, 10), 10)))