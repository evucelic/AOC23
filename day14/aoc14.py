from collections import defaultdict, Counter, deque
import sys
import re

input_path = "input.txt"

D = open(input_path, "r").read().split("\n")

columns = ["".join(c) for c in zip(*D)]

res = 0
end_pattern = re.compile(r"^[^#]*#*$")  # provjerava ima li # samo na kraju stupca

for col in columns:
    if end_pattern.match(col):
        for i in range(Counter(col)["O"]):
            res += len(col) - i
        continue
    hsh_idx = [i for i, c in enumerate(col) if c == "#"]
    start = 0
    for idx in hsh_idx:
        end = idx
        ctr = Counter(col[start:end])["O"]
        for j in range(ctr):
            res += len(col) - start - j
        start = idx + 1

    out_ctr = ctr = Counter(col[end : len(col)])["O"]
    for k in range(out_ctr):
        res += len(col) - end - k - 1

print(res)
