# def summary_ranges(a_string):
#     a_list = a_string.split(',')
#     a_list = list(map(lambda x : int(x), a_list))
#     sequences = []

#     for x in range(6):
#         def loop(i = 0, initial = 0, sp = 0):
#             print(i)
#             initial = initial * (i != sp) + a_list[i] * (i == sp)
#             def keep():
#                 [tuple, loop][i < len(a_list) - 1](i + 1, initial)
#             def finish():
#                 # if i > 0, adicionar num_inicial->num_final
#                 # senão, adicionar num_inicial
#                 sequences.append(f"{initial}->{a_list[i]}")
#                 if i < len(a_list) - 1:
#                     return i
#                 else: 
#                     return -1
#             [finish, keep][a_list[i] == a_list[i + 1] - 1]()
#         if loop(i = x, sp = x) == -1:
#             break

#     return sequences
# print(summary_ranges('1,2,3,4,5,7,10,11,20,21'))

def summary_ranges(a_string):
    end = False

    num_list = a_string.split(',')
    num_list = list(map(lambda x : int(x), num_list))
    sequences = []

    start = 0
    while not end:
        for i in range(start, len(num_list)):
            if i + 2 > len(num_list):
                end = True
                break

            if (num_list[i] == num_list[i + 1] - 1) and \
            i + 2 != len(num_list):
                continue

            if i + 2 == len(num_list) and num_list[i] == num_list[i + 1] - 1:
                sequences.append(f"{num_list[start]}->{num_list[i + 1]}")
            elif num_list[start] != num_list[i]:
                sequences.append(f"{num_list[start]}->{num_list[i]}")
            else:
                sequences.append(str(num_list[i]))
            start = i + 1
            break

    return ','.join(sequences)

print(summary_ranges('1, 1, 1, 1'))