# returns the common prefix between 2 words
def common_pref(str1, str2):
    pref = ""    
    for ch1, ch2 in zip(str1, str2):
        if ch1 == ch2:
            pref += ch1
    return pref

def longest_prefix(words):
    if len(words) <= 1:
        return words
    
    middle = len(words) // 2
    left = words[:middle]
    right = words[middle:]

    print(left, right)

    if len(left) == 2 and len(right) == 2:
        l_prefix = common_pref(left[0], left[1])
        r_prefix = common_pref(right[0], right[1])
        return common_pref(l_prefix, r_prefix)
    else: return common_pref(longest_prefix(left), longest_prefix(right))

print(longest_prefix(['sedatesingratiateconcomitant', 
    'sedatesparleypoliteness', 'sedateselbowsHahn', 
    "sedatesgloweringimbecility's", 'sedatesbuttershexing', 
    "sedatesKwangju'smulch's", 'sedatesunwiserN', 
    'sedatesprepossessedboggles', 
    'sedatesinterrelationshipdialings', "sedatesgropesNelsen's"]))


# def longest_prefix(words):
#     if len(words) == 1:
#         return words[0]
#     mid = len(words) // 2
#     left_prefix = longest_prefix(words[:mid])
#     right_prefix = longest_prefix(words[mid:])

#     i = 0
#     while i < len(left_prefix) and i < len(right_prefix) and left_prefix[i] == right_prefix[i]:
#         i += 1

#     return left_prefix[:i]
