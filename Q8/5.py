# def check_adjacent(pos1, pos2):
#         if (ord(pos1[0]) == ord(pos2[0]) + 1 or ord(pos1[0]) == ord(pos2[0]) -1) \
#             and (int(pos1[1]) == int(pos2[1])):
#             return True
#         if (int(pos1[1]) == int(pos2[1]) + 1 or int(pos1[1]) == int(pos2[1]) -1) \
#             and (ord(pos1[0]) == ord(pos2[0])):
#             return True
#         return False

# def soup(matrix, word):
#     if len(word) == 0:
#         return None

#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if word[0] == matrix[i][j]:
#                 pos = f"{chr(i + 65)}{j + 1}"
#                 next_pos = soup(matrix, word[1:])
#                 if next_pos:
#                     if check_adjacent(next_pos, pos):
#                         return pos
#                 elif len(word) == 1:
#                     return pos

def soup(matrix, word):
    pass



zopa = [['X', 'R', 'Z', 'B', 'H', 'A'], 
        ['K', 'A', 'S', 'I', 'G', 'O'], 
        ['J', 'O', 'T', 'C', 'A', 'N'], 
        ['D', 'P', 'O', 'O', 'X', 'F'], 
        ['Z', 'B', 'B', 'W', 'F', 'S']]

print(soup(zopa, 'PORTO'))


# for each row:
    # look for char
    # if char is found:
        # look for next char in a position that is adjacent to found char
        # if no char is found:
            # start over from the beginning in the next row
        # if char is found:
            # look for next char in a position that is adjacent to found char
            # return the current position