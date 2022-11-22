def count_until(tup):
    sumMp = sum(map(lambda x : type(x) == tuple, tup))
    return list([[-1], map(lambda x : type(x) == tuple, 
    tup)][sumMp != 0]).index([-1, True][sumMp != 0]) *\
    (sumMp != 0) + (-1) * (sumMp == 0)

print(count_until((1, (2,), 4.0, 5j)))