input_path = "input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

sum = 0

# first = next(filter(str.isdigit, "chasdsa3hsajdaj8aa"))
# last = next(filter(str.isdigit, "chasdsa3hsajdaj8aa"[::-1]))

# sum += int(first + last)

for line in lines:
    first = next(filter(str.isdigit, line))
    last = next(filter(str.isdigit, line[::-1]))

    sum += int(first + last)

print(sum)
