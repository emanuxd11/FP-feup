def sort_by_value(adict):
    l = list(adict.items())
    l.sort(key = lambda a : a[1])
    return l

print(sort_by_value({'Blue': '#0000FF', 'Red': '#FF0000', 'Green': '#008000', 'Black': '#000000', 'White': '#FFFFFF', 'Gray': '#808080'}))