n1 = abs(int(input()))
n2 = abs(int(input()))
result = 0

while True:
    if n1 > 0:
        result = 10*result + n1%10
        n1 = int(n1 / 10)
    if n2 > 0:
        result = 10*result + n2%10
        n2 = int(n2 / 10)

    if n1 <= 0 or n2 <= 0:
        break

print(result)