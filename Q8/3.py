def max_path(tree):
    if type(tree) == int:
        return tree

    left = tree[0]
    value = tree[1]
    right = tree[2]

    return max(max_path(left) + value, value + max_path(right))

print(max_path(((2, 1, ((1, 2, 2), 2, 1)), 0, (5, 4, 2))))