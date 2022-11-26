def magic_square(n):
    # create "empty" n*n matrix
    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(None)
        matrix.append(line)

    # start the algorithm
    i = 0
    j = n // 2
    matrix[i][j] = 1
    number = 2
    while number <= n**2:
        # get new positions for i and j according to the rules
        i -= 1
        j += 1

        # make sure i and j are in valid positions
        if (i < 0) and (j > n - 1):
            # print("the new condition")
            i += 2
            j -= 1
        if i < 0:
            i = n - 1
        if j > n - 1:
            j = 0
        if matrix[i][j]:
            # print(f"moved i to {i + 2} because {matrix[i][j]} was already there")
            i += 2
            j -= 1

        # position the numbers inside the matrix
        # print(f"printing {number} to {i, j}")
        matrix[i][j] = number
        number += 1
    
    return matrix

def print_matrix(matrix):
    for line in matrix:
        print(line)

try:
    print_matrix(magic_square(5))
except:
    print("fucked up lmao")
    