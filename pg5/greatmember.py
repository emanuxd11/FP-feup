def sum_values(chars):
    return sum(list(map(lambda x : ord(x), list(chars))))

def greatest_member(a_tuple, f = False):
    sums = []
    def loop(i = 0):
        def recall():
            sums.append((greatest_member(a_tuple[i], True)))
        def do_sum():
            sums.append(sum_values(a_tuple[i]))
        [do_sum, recall][type(a_tuple[i]) == tuple]()
        [int, loop][i < len(a_tuple) - 1](i + 1)
    loop()

    return [a_tuple[sums.index(max(sums))], sum(sums)][f]

print(greatest_member((('ab', 'dez', ('1',)), ('ab', 'de', ('1',)), 'defg', 'jkab')))