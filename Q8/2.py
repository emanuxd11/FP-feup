def flatten(alist):
    if len(alist) == 0:
        return []
    
    if type(alist[0]) == list:
        return flatten(alist[0]) + flatten(alist[1:])
    return [alist[0]] + flatten(alist[1:])    

print(flatten(['Hello', [2, [[], False]], [True]]))