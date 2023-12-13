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

for x,card in enumerate(winning):
    score = 0
    for number in card:
        if number in your[x]:
            score = score + 1 if score == 0 else score*2
    result += score

print(result)
