def magic(mat):
    n = len(mat)
    
    def check_lins(prev_sum = 0, curr_sum = 0):
        for i in range(n):
            curr_sum = sum(mat[i])
            if i != 0 and curr_sum != prev_sum:
                return False
            prev_sum = curr_sum
        return curr_sum
    lin_check = check_lins()
    if not lin_check:
        return False

    def check_cols(prev_sum = 0, curr_sum = 0):
        for i in range(n):
            curr_sum = sum([mat[j][i] for j in range(n)])
            if i != 0 and curr_sum != prev_sum:
                return False
            prev_sum = curr_sum
        return curr_sum
    col_check = check_cols()
    if not col_check:
        return False
    
    def check_diag(upward_sum = 0, downward_sum = 0):
        for i in range(n):
            upward_sum += mat[i][i]
            downward_sum += mat[i][n - i - 1]
        if upward_sum != downward_sum:
            return False
        else:
            return upward_sum
    diag_check = check_diag()
    if not diag_check:
        return False
    
    return col_check == lin_check == diag_check

print(magic([[17, 24, 1, 8, 16], [23, 5, 7, 15, 16], [4, 6, 14, 20, 22], [10, 13, 19, 21, 3], [12, 18, 25, 2, 9]]))
