n = int(input())

for i in range(n, 0, -1):
    numbers = [range(i, 0, -1)]
    print(", ".join(numbers))