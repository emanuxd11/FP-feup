def var_numbers(number, precision = 2):
    list = [*range(1, number + 1)]
    average = sum(list) / len(list)
    
    total_sum = 0
    for i in range(1, number + 1):
        total_sum += (i - average)**2
    
    return round(total_sum / number, precision)

print(var_numbers(3))