DIRECTIONS = {
    'E' : lambda row, col : (row, col + 1), 
    'N' : lambda row, col : (row - 1, col), 
    'W' : lambda row, col : (row, col - 1), 
    'S' : lambda row, col : (row + 1, col)
}

def move_ball(board):
    traveled = []
    initialPos = (0, 0)
    direction = ""

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in list(DIRECTIONS.keys()):
                initialPos = (i, j)
                direction = board[i][j]
                
    traveled.append(initialPos)
    i, j = initialPos

    while board[i][j] != 'X':
        if board[i][j] == '\\':
            if direction == 'E':
                direction = 'S'
            elif direction == 'N':
                direction = 'W'
            elif direction == 'W':
                direction = 'N'
            elif direction == 'S':
                direction = 'E'
        elif board[i][j] == '/':
            if direction == 'E':
                direction = 'N'
            elif direction == 'N':
                direction = 'E'
            elif direction == 'W':
                direction = 'S'
            elif direction == 'S':
                direction = 'W'

        position = (i, j)
        nextPosition = DIRECTIONS[direction](position[0], position[1])
        traveled.append(nextPosition)
        i, j = nextPosition

        # For visualization
        print(nextPosition, board[i][j])

    return traveled

# print(move_ball(['E \\', '/ /', '   ', '\\ X']))
print(move_ball(['/\\/\\X', ' \\/\\W', '\\   /']))