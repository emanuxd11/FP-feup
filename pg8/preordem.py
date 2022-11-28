def preorder(tree):
    if len(tree) < 2:
        return

    result = []

    val = tree[0]
    left = tree[1]
    right = tree[2]

    if type(val) is tuple:
        elem = preorder(val)
        result += elem
    else:
        result.append(val)
        
    if type(left) is tuple:
        elem = preorder(left)
        result += elem
    else:
        result.append(left)

    if type(right) is tuple:
        elem = preorder(right)
        result += elem
    else:
        result.append(right)
    
    return list(filter(lambda x : x is not None, result))
    

search = (2, (7, (2, None, None), (6, (5, None, None), (11, None, None))), (5, None, (9, (4, None, None), None)))

print(preorder(search))