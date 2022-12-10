def comprehensions(i, j):
    # first part
    the_list = [n for n in range(i, j + 1) 
        if int(str(n)[len(str(n)) - 1]) in [3, 8]]
    
    # second part
    the_tuple = tuple(round(n**0.5, 2) for n in range(i, j + 1))
    
    # third part
    the_dict = {n : chr(n) for n in range(i, j + 1)}
    
    return (the_list, the_tuple, the_dict)


print(comprehensions(110, 115))