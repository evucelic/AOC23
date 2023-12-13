input_path = "input.txt"

solution_dict = dict()

with open(input_path, "r") as file:
    lines = file.readlines()

#parse

for line in lines:
    game_no = int(line.split(":")[0].split(" ")[1])
    outcome_list = list()
    for split in line.split(":")[1].split(";"):
        set_dict = dict()
        for spl in split.split(","):
            set_dict.update({spl.strip().split(" ")[1] : int(spl.strip().split(" ")[0])})
        outcome_list.append(set_dict)
    solution_dict.update({game_no : outcome_list})

result = 0

for name, value in solution_dict.items():
    counter = 0
    for i in range(len(value)):
        if (value[i].get("green", 0) <= 13 and value[i].get("red", 0) <= 12 and value[i].get("blue", 0) <= 14):
            counter += 1
    if(counter == len(value)):
        result += name

print(result)
            