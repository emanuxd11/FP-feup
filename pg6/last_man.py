def last_man_standing(a_list, step):
    step -= 1
    def cycler(i = 0):
        def actually(n):
            nonlocal i
            i = (i + step) % len(a_list)
            a_list.pop(i)
            cycler(i)
        [int, actually][len(a_list) > 1](0)
    cycler()

    return a_list[0]

print(last_man_standing([3, 4, 1, 6, 2, 5, 7], 3))