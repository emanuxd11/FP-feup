import functools

def bounding_box(pts):
    x_max = functools.reduce(lambda x1, x2 : x1 if x1 > x2 else x2, map(lambda t : t[0], pts))
    x_min = functools.reduce(lambda x1, x2 : x1 if x1 < x2 else x2, map(lambda t : t[0], pts))
    y_max = functools.reduce(lambda y1, y2 : y1 if y1 > y2 else y2, map(lambda t : t[1], pts))
    y_min = functools.reduce(lambda y1, y2 : y1 if y1 < y2 else y2, map(lambda t : t[1], pts))

    return (x_min, y_min, x_max, y_max)

# print(bounding_box([(0,0), (1,1), (2,2), (3,3)]))


names = ['a', 'b', 'c']
ages = [1, 2, 3]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")