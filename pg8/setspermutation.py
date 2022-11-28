def permutations(tup):
    res = set()

    if len(tup) == 1:
        res.add(tup)
    elif len(tup) == 2:
        res.add(tup)
        res.add((tup[1], tup[0]))
    else:
        
        res.update(permutations(tup[1:]))
        res.update(permutations(tup[:len(tup) - 1]))
    return res

print(permutations(('A', 'B', 'C')))