import operator


def distribute(adict, op):
    keys = list(adict.keys())
    
    l = []
    for key in keys:
        if adict[key]:
            for val in adict[key]:
                l.append(op(key, val))
        else:
            l.append(key)
    
    return l
    
    # return [op(key, val) 
    #     if adict[key]
    #     else key
    #     for key in keys
    #     for val in adict[key]]



print(list(distribute({1:[0.1,0.5], 2:[], 3:[0,0.75]}, operator.add)))