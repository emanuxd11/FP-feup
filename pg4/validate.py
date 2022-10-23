# def false(n):
# 	return False

# def check_range(n):
# 	return n >= 0.0 and n <= 100.0

# def validate(grade):
# 	types = {int : True, float : True, bool : False, str : False}
# 	is_validType = types[type(grade)]
# 	print(is_validType)

# 	functionCalls = {bool : false, str : false, int : check_range, float : check_range}
# 	is_inRange = functionCalls[type(grade)](grade)

# 	return is_validType and is_inRange

# print(validate('X'))     



def validate(grade):
	try:
		return grade > 0.0 and grade < 100.0
	except:
		return False
	
print(validate('12'))                