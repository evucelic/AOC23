input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

winning = []
your = []
result = 0


for line in lines:
    c1 = line.split("|")
    card2 = c1[1].strip().split(" ")
    card1 = c1[0].split(":")[1].strip().split(" ")
    
    card1 = [x for x in card1 if x!=""]
    card2 = [x for x in card2 if x!=""]
    

    winning.append(card1)
    your.append(card2)

cards = [1]*len(lines)


for c,l in enumerate(winning):
    matches = 0
    for number in l:
        if number in your[c]:
            matches+=1
    
    for i in range(matches):
        cards[c+i+1] += cards[c]
        # c = 1
        # matches = 4
        # c[2] += c[1]
        # c[3] += c[1] ...

print(sum(cards))
