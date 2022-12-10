def x_union(list1, list2):
    result = list1 + list2
    l10 = list(map(lambda x : x[0], list1))
    l20 = list(map(lambda x : x[0], list2))
    result = filter(lambda t : not (t[0] in l10 and t[0] in l20), result)
    return list(result)

print(x_union([('a', 'b'), ('b', 'c')], [('b', 'b'), ('c', 'b')]))