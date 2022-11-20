def sparse_dot_product(dict1, dict2):
    dotp = 0

    for k1 in dict1:
        if k1 in dict2:
            dotp += dict1[k1] * dict2[k1]
    
    return dotp

print(sparse_dot_product({1: 3, 7: 1}, {1: 3, 7: 1}))