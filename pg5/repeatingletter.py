def repeated_letter(s, i = 0):
    def abc(a, b):
        return a[b - 1]
    def cba(a, b):
        return None
    return [[abc, repeated_letter][s.count(s[i]) == 1], 
    cba][i == len(s) - 1](s, i + 1)


print(repeated_letter("like"))