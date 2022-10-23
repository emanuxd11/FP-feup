senary = int(input())

decimal = 0
i = 0
while senary:
    decimal += (senary % 10) * 6**i
    senary = int(senary / 10)
    i += 1

print(decimal)