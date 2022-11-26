def is_pair_of_square(number_one, number_two):
    if number_one == number_two:
        return False
    if str(number_one)[::-1] != str(number_two):
        return False
    if str(number_one ** 2)[::-1] == str(number_two ** 2):
        return True
    return False