from collections import defaultdict, Counter, deque
import sys
import re

input_path = "input.txt"

D = open(input_path, "r").read().split("\n")
F = []
for row in D:
    temp = row.split()
    F.append((temp[0], temp[1].split(",")))

res = 0

DP = {}

def f(line, counts, i, ci, current):
    key = (i, ci, current)
    if key in DP:
        return DP[key]
    if i==len(line):
        if ci == len(counts) and current == 0:
            return 1
        elif ci == len(counts) - 1 and counts[ci] == current:
            return 1
        else:
            return 0
    ans = 0
    for c in [".", "#"]:
        if line[i] == c or line[i] == "?":
            if c == "." and current == 0:
                ans += f(line, counts, i+1, ci, 0)
            elif c == "." and current > 0 and ci<len(counts) and counts[ci] == current:
                ans+= f(line, counts, i+1, ci+1, 0)
            elif c == "#":
                ans += f(line, counts, i+1, ci, current + 1)
    DP[key] = ans
    return ans

for el in F:
    line = el[0]
    counts = [int(x) for x in el[1]]
    line  =  "?".join([line,line,line,line,line])
    counts *= 5
    DP.clear()
    res += f(line, counts, 0, 0, 0)

print(res)