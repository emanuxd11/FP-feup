def rearrange(l):
    # non_positive = [n for n in l if n <= 0]
    # positive = [n for n in l if n > 0]
    # return non_positive + positive
    return sorted(l, key = lambda x:x>0)

print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))