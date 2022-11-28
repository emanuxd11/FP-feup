def complete_pairs(s1, s2):
    alpha = set("abcdefghijklmnopqrstuvwxyz")
    result = set()
    for string1 in s1:
        for string2 in s2:
            if set(string1 + string2) == alpha:
                result.add(string1 + string2)
    return result

print(complete_pairs({'abcdefgh', 'lmnopqrst', 'abc', 'geeksforgeeks'}, {'abcdefghijklmnopqrstuvwxyz', 'ijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyz'}))