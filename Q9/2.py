def differences(alist):
    return list(map(lambda x, y : y - x, alist, alist[1:]))

print(differences([1, 2, 3, 4]))