def sort_pairs(alist):
    alist = sorted(alist, key=lambda t : (t[1], t[0]))
    return alist

print(sort_pairs([("Francisco", 30), ("Miguel", 25)]))