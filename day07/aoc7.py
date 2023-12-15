import math
input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

hands = []
bids = []
complete = []
sum = 0

hierarchy = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}

combinations = {
    "high_card": 1,
    "pair": 2,
    "two_pair": 3,
    "three": 4,
    "full_house": 5,
    "four": 6,
    "five": 7
}

def hand_judge(hand: str):
    allcards = [f for f in hand]
    allunique = set(allcards)

    pairs = [f for f in allunique if allcards.count(f) == 2]

    if len(allunique) == 1:
        return "five"

    if len(allunique) == 2:
        for f in allunique:
            if allcards.count(f) == 4 or allcards.count(f) == 1:
                return "four"

    if len(allunique) == 2:
        for f in allunique:
            if allcards.count(f) == 3 or allcards.count(f) == 2:
                return "full_house"
    
    for f in allunique:
        if allcards.count(f) == 3:
            allunique.remove(f)
            return "three"
        
    if(len(pairs) == 2):
        return "two_pair"
    
    if(len(pairs) == 1):
        return "pair"
    
    return "high_card"

def kicker(hand: str):
    return [combinations[hand_judge(hand)]] + ["23456789TJQKA".index(c) for c in hand]

for line in lines:
    hands.append(line.split(" ")[0])
    bids.append(int(line.split(" ")[1]))

for x,hand in enumerate(hands):
    rank = hand_judge(hand)
    complete.append((combinations[rank], bids[x], hand))


sorted_list = sorted(complete, key= lambda x: (x[0], kicker(x[2])))


for num, element in enumerate(sorted_list):
    sum += (num+1) * element[1]

print(sum)
    


