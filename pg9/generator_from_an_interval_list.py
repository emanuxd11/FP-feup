def generator(intlist):
    for el in intlist:
        for i in range(el[0], el[1] + 1):
            yield i

print(list(generator([(1, 1), (3, 5), (10, 15)])))