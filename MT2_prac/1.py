def next_leap_year(y):
    next_y = y
    while True:
        next_y += 1
        if next_y % 400 == 0:
            return next_y
        if next_y % 4 == 0:
            # don't need to check whether it is
            # divisible by 400 because we already
            # know it didn't pass the first condition
            if (next_y % 100 != 0):
                return next_y

print(next_leap_year(2004))