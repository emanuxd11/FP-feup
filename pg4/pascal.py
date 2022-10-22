import  math

def pascal(n):
    for i in range(0, n):
        for j in range(0, n):
            print(str(math.factorial(i) / (math.factorial(j) * math.factorial(i - j))), end = " ")
        print("")

pascal(3)