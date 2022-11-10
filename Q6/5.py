def mult(M, N):
    if len(M[0]) != len(N):
        return []
    
    n_linhasPr = len(M)
    n_colunaSe = len(N[0])

    def dotp(v1, v2):
        n = len(v1)
        return sum([v1[i] * v2[i] for i in range(n)])    
    
    def get_col(mat, col):
        row = []
        for i in range(len(mat)):
            row.append(mat[i][col])
        return row

    matriz_final = []
    for lin in range(n_linhasPr):
        linha = []
        for col in range(n_colunaSe):
            linha.append(dotp(M[lin], get_col(N, col)))
        matriz_final.append(linha)

    return matriz_final

print(mult([[1, 2], [3, 4]], [[2, 0], [1, 2]]))
