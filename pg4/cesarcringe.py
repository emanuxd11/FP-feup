def fib(n):
    return int(((1 + 5**0.5)**n - (1 - 5**0.5)**n) // (2**n * 5**0.5))

def caesar(message):
    result = ""
    for i in range(len(message)):
        result += chr((ord(message[i]) - 65 - fib(i)) % 26 + 65) * message[i].isalpha() + message[i] * (not message[i].isalpha())
    return result

print(caesar("HELLO WORLD!"))
