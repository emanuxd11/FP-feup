def count_chars(string, character):
    n = string.count(character)
    return -1 * int(n == 0) + n

print(count_chars("How much wood would a woodchuck chuck if a woodchuck could chuck wood?", 'w'))