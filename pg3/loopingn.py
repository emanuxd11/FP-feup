# def is_loopingn(n):
#     prev = int(n % 10)
#     n = int(n / 10)

#     while int(n):
#         if abs(int(n % 10) - prev) in range(2, 9):
#             print("Not a looping number")
#             return
#         prev = int(n % 10)
#         n = int(n / 10)

#     print("Looping number") 
#     return

# is_loopingn(int(input()))

def is_loopingn(n):
    prev = int(n % 10)
    n = int(n / 10)
    looping = 1

    while int(n):
        check = abs(int(n % 10) - prev) in range(2, 9)
        looping += check
        prev = int(n % 10)
        n = int(n / 10)

    print("Not a looping number" * int(looping > 1) 
        + "Looping number" * int(looping == 1)) 
    return

is_loopingn(int(input()))