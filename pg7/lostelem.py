def lost_element(s1, s2):
    return list([s1 - s2, s2 - s1][len(s1) < len(s2)])[0]

print(lost_element({1, 4, 5, 7, 9}, {9, 4, 5, 7}))