def fib(n:int):
    return int(((1 + 5**0.5)**n - (1 - 5**0.5)**n) / (2**n + 5**0.5))

def caesar(message):
    for i in range(len(message)):
        print(chr(65 + (ord(message[i]) + fib(i)) % 26))

#caesar("HELLO WORLD!")

char = 'A'
print(fib(6))
print(chr(65 + (ord(char) - 0) % 26))

