import random
from typing import List, Tuple

# card suits
SUITS = "♠ ♡ ♢ ♣".split()  # spade, heart, diamond, club
# card ranks
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()  # 2-10, Jack, Queen, King, Ace

Card = Tuple[str, str]
Deck = List[Card]

def card_value(card):
    if card[1] in ['J', 'Q', 'K']:
        value = 10
    elif card[1] == 'A':
        value = 11
    else:
        value = int(card[1])

    if card[0] in ['♠', '♣']:
        value *= 2

    return value

def create_deck(shuffle: bool = False) -> Deck:
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def choose(items):
    return random.choice(items)

def player_order(names, start=None):
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

def play(seed_value):
    random.seed(seed_value)
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)
    points = {"P1" : 0, "P2" : 0, "P3" : 0, "P4" : 0}
    maxPoints = 0
    winners = ""

    while hands[start_player]:
        maxVal = 0
        maxNames = []

        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)

            # Get the player with highest 
            # card value count for the round
            currentValue = card_value(card)
            if currentValue > maxVal:
                maxVal = currentValue
                maxNames = [name]
            elif currentValue == maxVal:
                maxNames.append(name)
        
        # Increase the score of round winners
        for player in maxNames:
            points[player] += 1
    
    # Get the highest scoring players
    # at the end of the game
    for player in points:
        if points[player] > maxPoints:
            maxPoints = points[player]
            winners = player
        elif points[player] == maxPoints:
            winners += f" {player}"

    return winners

# # # # # # #
print(play(999))