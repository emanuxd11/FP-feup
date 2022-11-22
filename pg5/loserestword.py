def longest(s):
    return len(max(s.split(), key=len))

print(longest("Unnecessarily blah blaj"))