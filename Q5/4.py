def multi(g):
    result = ()

    for double in g:
        newtup = (double[0], g.count(double), double[1])
        if newtup not in result:
            result += (newtup,)
        
    return tuple(result)
print(tuple(multi((('A','B'),('A','C'),('B','C'),('C','B'),('A','B')))))

