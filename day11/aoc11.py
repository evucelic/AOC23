from collections import defaultdict, Counter, deque
import sys
import re

input_path = "input.txt"

D = open(input_path, "r").read().split("\n")

empty_row = [
    r for r, row in enumerate(D) if all(c == "." for c in row)
]  # indeksi praznih redova
empty_column = [
    c for c, col in enumerate(zip(*D)) if all(c == "." for c in col)
]  # indeksi praznih stupaca

sum = 0

galaxy = [(i, j) for i in range(len(D)) for j in range(len(D[0])) if D[i][j] == "#"]

for r, g1 in enumerate(galaxy):
    for l, g2 in enumerate(galaxy[:r]):
        dist = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])  # Manhattan distance calculation
        for r in empty_row:
            if (
                min(g1[0], g2[0]) < r < max(g1[0], g2[0])
            ):  # Ako je prazna linija izmedu koordinata dodaj 1
                dist += 1
        for c in empty_column:
            if min(g1[1], g2[1]) < c < max(g1[1], g2[1]):
                dist += 1
        sum += dist

print(sum)
