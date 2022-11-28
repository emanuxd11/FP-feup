# def most_frequent(l):
#     d = {}
#     max_occurrence = -1
#     d = {}
#     for n in l:
#         d[n] = l.count(n)
#         if d[n] > max_occurrence:
#             max_occurrence = d[n]
#             max_val = n
#         elif d[n] == max_occurrence:
#             if n > max_val:
#                 max_val = n
#     return max_val

def most_frequent(alist):
    l1 = list(dict.fromkeys(alist))
    l1 = sorted(l1, reverse=True)
    print(l1)
    l2 = list(map(lambda i: alist.count(l1[i]), list(range(len(l1)))))
    print(l2)
    return l1[l2.index(max(l2))]


print(most_frequent([0, 0, 2, -1]))
