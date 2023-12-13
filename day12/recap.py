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

K = {}
def f(line, block, i, bi, current):
    key = (i, bi, current)
    if key in K:
        return K[key]
    if i == len(line):
        if bi == len(block) and current == 0:
            return 1
        elif bi == len(block) - 1 and block[bi] == current:
            return 1
        else:
            return 0
    ans = 0
    for c in ["#", "."]:
        if line[i] == "?" or line[i] == c:
            if c == "." and current == 0:
                ans += f(line, block, i+1, bi, 0)
            elif c == "." and current > 0 and bi < len(block) and block[bi] == current:
                ans += f(line, block, i+1, bi+1, 0)
            elif c == "#":
                ans += f(line, block, i+1, bi, current+1)
    K[key] = ans
    return ans

for el in F:
    line = el[0]
    line = "?".join([line,line,line,line,line])
    counts = [int(x) for x in el[1]]
    counts *= 5
    K.clear()
    res += f(line, counts, 0, 0, 0)

print(res)

