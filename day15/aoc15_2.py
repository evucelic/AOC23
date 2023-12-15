from collections import defaultdict, Counter, deque
import sys
import re

input_path = "input.txt"

D = open(input_path, "r").read().strip().split(",")

HASHMAP = [{} for _ in range(256)]


def HASH(string: str) -> int:
    current = 0
    for c in string:
        current += ord(c)
        current *= 17
        current = current % 256

    return current


for d in D:
    if "-" in d:
        key = d.split("-")[0]
        HASHMAP[HASH(key)].pop(key, -1)
    else:
        key, value = d.split("=")
        HASHMAP[HASH(key)][key] = int(value)

res = 0
for idx, elem in enumerate(HASHMAP):
    for lens_idx, (k, v) in enumerate(elem.items()):
        res += (idx + 1) * (lens_idx + 1) * v

print(res)
