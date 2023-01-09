def to_celsius(t):
    return list(map(lambda x : round((x - 32) / 1.80, 1), t))