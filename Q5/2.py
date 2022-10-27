def camel_case(phrase):
    result = ""
    toupper = False
    for i in range(len(phrase)):
        if not phrase[i].isalpha():
            toupper = True
        elif not toupper:
            result += phrase[i].lower()
        if toupper and phrase[i].isalpha():
            result += phrase[i].upper()
            toupper = False
    
    return result

print(camel_case("testing"))