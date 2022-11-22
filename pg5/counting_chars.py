def count_chars(a_string):
    alpha   = sum(map(lambda x : x.isalpha(), a_string))
    digit   = sum(map(lambda x : x.isdigit(), a_string))
    special = sum(map(lambda x : (not x.isalpha()) * (not x.isdigit()), a_string))
    return (alpha, digit, special)

print(count_chars('Str1nG$'))