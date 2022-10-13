def print_square(size):
    if(size < 3):
        return
    
    if size % 2 == 0:
        center = range(int(size/2) - 1, int(size/2) + 1)
    else:
        center = [int(size/2)]

    for i in range(0, size):
        for j in range(0, size):
            if i in center and j in center:
                print('0', end = "")    
            else:
                print('#', end = "")
        print("")
        

print_square(abs(int(input())))