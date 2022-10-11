a = int(input())
b = int(input())

print((a + b) + (int((a - b) % 2) - 1) * (-a - b) + int((a - b) % 2) * (a * b))