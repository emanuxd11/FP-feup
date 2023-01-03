import random

def normalize(str1, str2):
    if len(str1) > len(str2):
        str2 += (len(str1) - len(str2)) * 'x'
    elif len(str2) > len(str1):
        str1 += (len(str2) - len(str1)) * 'x'
    return (list(str1), list(str2))

def cows_bulls(seed_value):
    random.seed(seed_value)
    correct = str(random.randint(0, 9999))

    def calculate(guess):
        nonlocal correct
        bulls = cows = 0

        print(guess, correct)

        # Calculate bulls
        correct, guess = normalize(correct, str(guess))
        for i in range(len(guess)):
            if guess[i] == correct[i]:
                bulls += 1
                guess[i] = correct[i] = None
        
        # Calculate cows
        for i in range(len(guess)):
            if guess[i] == None:
                continue
            if guess[i] in correct:
                cows += 1
                correct[correct.index(guess[i])] = None
                guess[i] = None

        return (cows, bulls)

    return calculate

	
print(cows_bulls(62678)(9887))