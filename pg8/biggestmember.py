def biggest_member(atuple):
    biggest_len = -1
    biggest = None
    def recurse(btuple):
        nonlocal biggest_len, biggest
        for member in btuple:
            def whatamidoinglmao(a):
                def do_attribute(a):
                    nonlocal biggest_len, biggest
                    biggest_len = len(member)
                    biggest = member
                [int, do_attribute][len(member) > biggest_len](0)
                recurse(member)
            [int, whatamidoinglmao][type(member) == tuple](0)
                
    recurse(atuple)

    return [biggest, atuple][biggest_len < len(atuple)]

print(biggest_member((1, (5, (6, 8), 3, 9), 2)))
