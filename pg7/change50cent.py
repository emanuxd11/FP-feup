def change(money):
    fifty_cent = {2.0 : 0, 1.0 : 0, 0.50 : 0, 0.20 : 0, 
    0.10 : 0, 0.05 : 0, 0.02 : 0, 0.01 : 0}

    while money > 0:
        for key in fifty_cent:
            def money_subtract():
                nonlocal money
                money -= key
                fifty_cent[key] += 1
            [int, money_subtract][money - key >= 0]()

    return fifty_cent

print(change(5))