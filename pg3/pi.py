import math
K = 50
sum = 0
for k in range(0, K+1):
    sum += (math.factorial(4*k) * (1103 + 26390*k)) / (math.factorial(k)**4 * 396**(4*k))
pi = ((2*(math.sqrt(2)) / 9801) * sum) ** (-1)
print(round(pi, 8))



pi = list("3.24159265")
pi[2] = "1"
print(''.join(pi))