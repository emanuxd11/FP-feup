def mastermind(g1, g2, g3, c1, c2, c3):
    guess = [g1, g2, g3]
    correct = [c1, c2, c3]
    counted = []
    points = 0

    for i in range(0, len(guess)):
        if guess[i] in correct:
            if guess[i] == correct[i]:
                counted.append(guess[i])
                points += 3
            elif i not in counted:
                if correct.count(guess[i]) == 1 and guess[i] in counted:
                    continue
                if guess.count(guess[i]) > correct.count(guess[i]) and guess[i] in  counted:
                    continue
                points += 1
                counted.append(guess[i])
    
    return points     

print(mastermind("a", "b", "c", "c", "b", "a"))           