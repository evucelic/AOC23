from collections import defaultdict, Counter
import sys
import re

input_path = "input.txt"

D = open(input_path, "r").readlines()

col = []

sum = 0

for line in D:
    col.append(line.strip().split(" "))

for l in col:
    distances = []
    br = idx  = 1
    distances.append(l)
    while br == 1:
        ff = []
        for i in range(len(l)):
            if i < len(l) - 1:
                ff.append(int(l[i+1]) - int(l[i]))
        distances.append(ff)
        l = ff
        if all(x == 0 for x in distances[idx]):
            br = 0
        idx += 1
    
    for m, element in enumerate(distances):
        m = 1 if m%2 == 0 else -1
        sum += m*int(element[0])
        

print(sum)