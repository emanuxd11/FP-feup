a = float(input())
b = float(input())
c = float(input())

delta = b*b -4*a*c

if(delta >= 0):
    print(f"The solutions are {round((-b + delta ** 0.5)/(2 * a), 2)} and {round((-b - delta ** 0.5)/(2 * a), 2)}")
else:
    print(f"The solution is {round((-b) / (2 * a), 2)}")