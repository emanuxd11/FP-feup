def longest_prefix(words):
    if len(words) == 1:
        return words[0]

    # proper recursion done here, using the "strategy" of pretending it 
    # is already implemented
    mid = len(words) // 2
    left_prefix = longest_prefix(words[:mid])
    right_prefix = longest_prefix(words[mid:])

    i = 0
    while i < len(left_prefix) and i < len(right_prefix) and left_prefix[i] == right_prefix[i]:
        i += 1

    return left_prefix[:i]


print(longest_prefix(['sedatesingratiateconcomitant', 
    'sedatesparleypoliteness', 'sedateselbowsHahn', 
    "sedatesgloweringimbecility's", 'sedatesbuttershexing', 
    "sedatesKwangju'smulch's", 'sedatesunwiserN', 
    'sedatesprepossessedboggles', 
    'sedatesinterrelationshipdialings', "sedatesgropesNelsen's"]))