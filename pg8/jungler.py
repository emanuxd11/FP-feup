def juggler(n, p):
    # if p == 0:
    #     return n

    # junglah = juggler(n, p - 1)
    # if junglah % 2 == 0:
    #     return int(junglah ** (0.5))
    # return int(junglah ** (1.5))

    return [lambda *_ : [int(juggler(n, p - 1) ** 0.5), int(juggler(n, p - 1) ** 1.5)][juggler(n, p - 1) % 2 != 0], int][p == 0](n)

print(juggler(3, 1))