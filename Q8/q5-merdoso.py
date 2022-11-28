def findNextLetter(matrix, word, row, ch):
    if len(word) > 0:
        if ch<5 and matrix[row][ch+1] == word[0]:
            if findNextLetter(matrix, word[1:], row, ch+1):
                return True
        if row<5 and matrix[row+1][ch] == word[0]:
            if findNextLetter(matrix, word[1:], row+1, ch):
                return True
        if ch>0 and matrix[row][ch-1] == word[0]:
            if findNextLetter(matrix, word[1:], row, ch-1):
                return True
        if row>0 and matrix[row-1][ch] == word[0]:
            if findNextLetter(matrix, word[1:], row-1, ch):
                return True
    else:
        return True

def soup(matrix, word):
    for row in range(len(matrix)):
        for ch in range(len(matrix)):
            if matrix[row][ch] == word[0]:
                if findNextLetter(matrix, word[1:], row, ch):
                    return (chr(ord("A")+row)+str(ch+1))

print(soup([['X', 'R', 'Z', 'B', 'H', 'A'], 
            ['K', 'A', 'S', 'I', 'G', 'O'], 
            ['J', 'O', 'T', 'C', 'A', 'N'], 
            ['F', 'S', 'R', 'H', 'T', 'U'], 
            ['D', 'P', 'O', 'O', 'X', 'F'], 
            ['Z', 'B', 'B', 'W', 'F', 'S']], 
            'TACHO'))