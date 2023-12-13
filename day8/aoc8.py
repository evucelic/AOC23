input_path = "input.txt"

P = open(input_path, "r").read()

dir, D = P.split("\n\n")

D = D.split("\n")

P1 = {"L": {}, "R": {}}
step_no = 0

for line in D:
    S = line.split("=")
    key = S[0].strip()
    g1, g2 = S[1].strip().split(",")
    g1 = g1[1:].strip()
    g2 = g2[:-1].strip()
    P1["L"][key] = g1
    P1["R"][key] = g2

start = "AAA"

while "ZZZ" != start:
    index = step_no % len(dir)  # 0 1 2 0 1 2 za LLR
    start = P1[dir[index]][start]
    step_no += 1

print(step_no)
