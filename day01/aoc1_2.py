input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

sum = 0

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


for line in lines:
    for i in range(len(line)):
            for name, value in digits.items():
                substring = line[:i]
                if name in substring:
                    line = line.replace(name, str(value))
    
    first = next(filter(str.isdigit, line))
    last = next(filter(str.isdigit, line[::-1]))
    sum += int(first + last)

print(sum-8)

