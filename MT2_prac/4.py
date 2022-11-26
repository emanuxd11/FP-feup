def unique_ntree(tree):
    if len(tree) == 0:
        return []

    unique = []
    for element in tree:
        if type(element) is tuple:
            unique += unique_ntree(element)
        else:
            unique.append(element)

    # When it comes to preserving order, this
    # is a good way to remove duplicates from
    # a list. Because here we are sorting it, 
    # it doesn't really make a difference and 
    # we could've just done list(set(unique))
    no_dup = list(dict.fromkeys(unique))
    no_dup.sort()
    return no_dup 

print(unique_ntree((1, (2, (), ()), (1, (), ()))))
print(unique_ntree((11, (), ((22, (), ((33, (), ((44, (), ((55, (), ())))))))))))
