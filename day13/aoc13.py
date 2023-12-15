from collections import defaultdict, Counter, deque
import sys
import re

input_path = "input.txt"

D = open(input_path, "r").read().split("\n")

F = []
tmp = []

for line in D:
    if line != "":
        tmp.append(line)
    if line == "":
        F.append(tmp)
        tmp = []


def check(grid):
    R = len(grid)
    C = len(grid[0])
    for c in range(C - 1):
        br = 0
        for dc in range(C):
            left = c - dc
            right = c + 1 + dc
            if 0 <= left < right < C:
                for r in range(R):
                    if grid[r][left] != grid[r][right]:
                        br += 1
        if br == 0:  # samo ako su svi isti
            return c + 1
    return 0


res = 0

for block in F:
    columns = ["".join(col) for col in zip(*block)]
    rows = block

    res += check(columns) * 100 + check(rows)

print(res)
