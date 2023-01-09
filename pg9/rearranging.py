from functools import reduce

def rearrange(l):
    pos_and_non_pos = reduce(
        lambda acc, x: acc[[0, 1][x > 0]].append(x) or acc,
        l,
        ([], [])
    )

    return pos_and_non_pos[0] + pos_and_non_pos[1]

print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))