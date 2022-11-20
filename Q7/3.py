def roman_to_integer(astring):
    integer_numeral = 0

    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    alist = list(astring)

    for i in range(len(alist)):
        if alist[i] not in romans:
            continue
        
        if i == len(alist) - 1:
            integer_numeral += romans[alist[i]]
            break
        
        if romans[alist[i]] < romans[alist[i + 1]]:
            integer_numeral -= romans[alist[i]]
        else:
            integer_numeral += romans[alist[i]]

    return integer_numeral

print(roman_to_integer('LXXXIV'))