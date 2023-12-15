input_path = "input.txt"

solution_dict = dict()

with open(input_path, "r") as file:
    lines = file.readlines()

# parse

for line in lines:
    game_no = int(line.split(":")[0].split(" ")[1])
    outcome_list = list()
    for split in line.split(":")[1].split(";"):
        set_dict = dict()
        for spl in split.split(","):
            set_dict.update({spl.strip().split(" ")[1]: int(spl.strip().split(" ")[0])})
        outcome_list.append(set_dict)
    solution_dict.update({game_no: outcome_list})

result = 0

for name, value in solution_dict.items():
    max_green = 0
    max_red = 0
    max_blue = 0
    for i in range(len(value)):
        if value[i].get("green", 0) > max_green:
            max_green = value[i].get("green", 0)
        if value[i].get("red", 0) > max_red:
            max_red = value[i].get("red", 0)
        if value[i].get("blue", 0) > max_blue:
            max_blue = value[i].get("blue", 0)
    result += max_blue * max_red * max_green

print(result)
