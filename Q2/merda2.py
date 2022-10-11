number = str(input())

for i in range(len(number)):
    print(number[i], end="")
    if number[i] != "0":
        for j in range(len(number) - i - 1):
            print("0", end="")
    print("")