def false(x):
    return False

def check_inRange(grade):
    return bool(int(grade >= 0) * int(grade <= 100))

def validate(grade):
    d = {False : false, True : check_inRange}
    return d[int(type(grade) == int) + int(type(grade) == float)](grade)


print(validate('1'))


# def validate(grade):
#    return (type(grade) == float or type(grade) == int) and (float(grade) >= 0 and float(grade) <= 100)

# print(validate(True))
# print(validate(False))
