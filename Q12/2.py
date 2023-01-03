def tic_tac_toe(board, player):
    boardMatrix = [[], [], []]
    
    line = 0
    for char in board:
        if char == '\n':
            line += 1
            continue
        if char == ' ':
            boardMatrix[line].append(None)
        else:
            boardMatrix[line].append(char)
    
    def check_row(row, player):
        if row.count(player) == 3:
            return True

    def check_col(col, player):
        for row in boardMatrix:
            if row[col] != player:
                return False
        return True

    def check_diag(boardMatrix, player):
        diag = True

        for i in range(len(boardMatrix)):
            if boardMatrix[i][i] != player:
                diag = False
        if diag == True:
            return True
        else:
            diag = True

        for i in range(len(boardMatrix)):
            if boardMatrix[i][len(boardMatrix) - i - 1] != player:
                diag = False
        if diag == True:
            return True

    for i in range(len(boardMatrix)):
        for j in range(len(boardMatrix)):
            if boardMatrix[i][j] == None:
                boardMatrix[i][j] = player

                if check_row(boardMatrix[i], player) or \
                    check_col(j, player) or \
                    check_diag(boardMatrix, player):
                    return f"{chr(ord('A') + i)}{j + 1}"
                else:
                    boardMatrix[i][j] = None

print(tic_tac_toe('xo \n xo\no  ', 'x'))