def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

def recursion_depth(number):
    print(f"{number}, ", end = "")
    recursion_depth(number + 1)

def recursive_sum(nested_list):
    total = 0
    for element in nested_list:
        if type(element) is list:
            total += recursive_sum(element)
        else:
            total += element
    return total

print(recursive_sum([1, 3, [2, 5, [7], 4]]))