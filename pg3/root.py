n = float(input())
lowerb = 0.0
upperb = n

while True:
    midp = (lowerb + upperb) / 2

    if midp*midp == n:
        break

    if midp*midp > n:
        upperb = midp
    else:
        lowerb = midp

    lowerdigits = str(lowerb).split('.')[1][:5]
    upperdigits = str(upperb).split('.')[1][:5]

    if lowerdigits == upperdigits:
        break

print(midp)

#doesn't work