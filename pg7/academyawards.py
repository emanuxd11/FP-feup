def academy_awards(alist):
    res = {}
    newl = []
    for tup in alist:
        newl.append(tup[1])
        res[tup[1]] = newl.count(tup[1])
    return res

print(academy_awards([('Best Picture', 'Moonlight'), ('Best Director', 'La La Land'), ('Best Actor', 'Manchester by the Sea'), ('Best Actress', 'La La Land'), ('Best Supporting Actor', 'Moonlight'), ('Best Supporting Actress', 'Fences'), ('Best Original Screenplay', 'Manchester by the Sea'), ('Best Original Score', 'La La Land')]))