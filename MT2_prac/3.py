def dict2list(adict, m, n):
    for key in adict:
        if key[0] >= m or key[1] >= n:
            return None

    neo = []
    for i in range(m):
        morpheus = []
        for j in range(n):
            if (i, j) in adict:
                morpheus.append(adict[(i, j)])
            else: 
                morpheus.append(0)
        neo.append(morpheus)
    return neo


print(dict2list({(0, 1): 4, (2, 1): 6}, 2, 3))