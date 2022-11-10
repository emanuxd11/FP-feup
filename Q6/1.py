def mastermind(guesses, codes):
    length     = len(guesses)
    corr_pos   = 0
    incorr_pos = 0

    for i in range(length):
        if guesses[i] == codes[i]:
            corr_pos += 1
            guesses[i] = codes[i] = None

    for i in range(length):
        if guesses[i] == None:
            continue
        if guesses[i] in codes:
            incorr_pos += 1
            codes[codes.index(guesses[i])] = None
            guesses[i] = None


    
    return (corr_pos, incorr_pos)

print(mastermind(["b", "b", "y"], ["b", "w", "b"]))