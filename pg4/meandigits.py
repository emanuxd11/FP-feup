def roundUp(n):
    return int(n + 0.5)

def digits_average(n):
    n1 = 0
    n2 = 0
    avg = 0
    counter = 999
    sum = 0

    while n > 9:
        n1 = n % 10
        n = n // 10
        n2 = n % 10
        prov_sum = avg
        avg = roundUp((n1 + n2) / 2)
        prov_sum += roundUp(avg / 2)    
        sum += prov_sum
        ##
        print(f"avg = {avg}, sum = {sum}\tn1 = {n1}, n2 = {n2}")
        
    return sum

print(digits_average(158))

