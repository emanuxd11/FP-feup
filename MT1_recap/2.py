n = str(input())
for i in range(0, len(n)):
    print(int(n[i]) * 10**(len(n) - 1 - i))
