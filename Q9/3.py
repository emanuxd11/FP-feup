def variance(alist):
    N = len(alist)
    avg = sum(alist) / N
    var = sum(map(lambda x : (x - avg)**2, alist)) / N
    return round(var, 3)

    	
print(variance([1, 2, 3, 4, 5, 6]))