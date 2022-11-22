def flatten(alist):
    ret_val = []

    if alist == []:
        return []
    
    if type(alist[0]) == list:
        ret_val += flatten(alist[0])
    elif len(alist) > 1:
        ret_val += alist[1:]

    return ret_val

print(flatten([[1,[2,3]], [4,[[5]],6], [7,8,9]]))