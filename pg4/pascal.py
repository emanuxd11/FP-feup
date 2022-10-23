import  math

def pascal(n):
    string = ""
    for i in range(0, n):
        for j in range(0, i+1):
            c = math.factorial(i)
            c = c // (math.factorial(j) * math.factorial(i - j))
            string += str(c) + " " * int(j != i)
        string += "\n"
    return string

print(pascal(10))