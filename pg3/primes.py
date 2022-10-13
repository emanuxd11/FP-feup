n1 = int(input())
n2 = int(input())
check = 0
primes = []

for i in range(abs(n1), abs(n2) + 1):
    check = 0
    for j in range(2, i):
        check += int(i % j == 0)
    primes.append(int(check == 0) * i)

primes = list(filter(lambda item: item != 0, primes))
print("Prime numbers between", n1, "and", n2, "are:", 
' '.join(map(str, primes)))