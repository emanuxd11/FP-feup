def find_me(f, limits):
    iterations = 0
    lowB = limits[0]
    upB = limits[1]

    while True:
        midVal = (upB + lowB) // 2

        if f(midVal) == 0:
            iterations += 1
            return iterations
        if f(midVal) == -1:
            upB = midVal - 1
            iterations += 1
        if f(midVal) == 1:
            lowB = midVal + 1
            iterations += 1

print(find_me(lambda n: -1 if n > 30 else 1 if n < 30 else 0, (0, 100)))