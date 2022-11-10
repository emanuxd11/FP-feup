def local_minima(alist):
    minima_list = []
    for i in range(len(alist) - 2):
        smallest = min(alist[i:i + 3])
        if alist[i:i+3].count(smallest) == 1:
            minima_list.append(smallest)
    return minima_list

print(local_minima([10, 3, 3, 14, 5, 7, 4]))