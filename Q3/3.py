n = abs(int(input()))
reverse = 0
while n != 0:
    reverse = 10*reverse + n%10
    n = int(n / 10)
print(reverse)