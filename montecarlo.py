import random

circle = 0; square = 0

for i in range(1000**2):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    distance = x**2 + y**2

    if(distance <= 1):
        circle += 1
    square += 1

pi = 4 * circle/square

print(pi)