def discard_middle(s):
    def aux(s):
        return s[0] + s[1] + s[len(s) - 2] + s[len(s) - 1]
    return [lambda s : ' ', aux][len(s) > 3](s)

print(discard_middle("st"))