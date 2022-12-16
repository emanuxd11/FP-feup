def bisect(f, n):
    lower = 0
    upper = 1

    for i in range(n):
        midPoint = (lower + upper) / 2
        if f(lower) * f(midPoint) >= 0:
            lower = midPoint
        else:
            upper = midPoint
        
    return round(midPoint, 5)

print(bisect(lambda x: (1-(x+0.2))*(x+0.2), 10))