def find_treasure(pos, steps):
    dirs = {
        "up" : lambda pos : (pos[0], pos[1] + 1),
        "right" : lambda pos : (pos[0] + 1, pos[1]),
        "left" : lambda pos : (pos[0] - 1, pos[1]),
        "down" : lambda pos : (pos[0], pos[1] - 1)
    }

    def recurse(i = 0):
        nonlocal pos
        def keep_recursing():
            nonlocal pos
            pos = dirs[steps[i]](pos)
            recurse(i + 1)
        [int, keep_recursing][i <= len(steps) - 1]()
    recurse()
    return pos


print(find_treasure((0, 0), ['up', 'up', 'left', 'right', 'up', 'up']))