from functools import reduce

def map_filter_reduce(lst, f1, f2, f3):
    return reduce(f3, map(f2, filter(f1, lst)))

print(map_filter_reduce([1, 2, 3, 4, 5, 6, 7, 8], lambda i: i % 2 == 0, lambda i: i**2, lambda a, b: a+b))