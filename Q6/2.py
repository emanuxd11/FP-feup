def change(amount):
    COINS = [200, 100, 50, 20, 10, 5, 2, 1]
    the_change = [0]

    while sum(the_change) < amount:
        for i in range(len(COINS)):
            if sum(the_change) + COINS[i] <= amount:
                the_change.append(COINS[i])
                break

    the_change.pop(0)
    the_change.sort(reverse=True)
    return the_change

print(change(345))