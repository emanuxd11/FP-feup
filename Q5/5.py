def triplet(tup):
    for i in range(len(tup)):
        for j in range(i + 1, len(tup)):
            for k in range(j + 1, len(tup)):
                if tup[i] + tup[j] + tup[k] == 0:
                    return (tup[i], tup[j], tup[k])
                
    return ()

print(triplet((-8, 0, 4, -2, -1, 1, 2)))