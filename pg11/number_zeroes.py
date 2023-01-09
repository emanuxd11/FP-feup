def count_zeroes(f):
    return f().count(0)

print(count_zeroes(lambda: [1]*8 + [0]*6))
