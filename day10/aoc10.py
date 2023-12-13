from collections import defaultdict, Counter, deque
import sys
import re

input_path = "input.txt"

D = open(input_path, "r").read().split("\n")

n,m = len(D), len(D[0])

def neigbours(i, j):
    res = []
    for di, dj in list(compute(i, j)):
        ii, jj = i + di, j + dj
        if not(0 <= ii < n and 0 <= jj < m):
            continue
        res.append((ii, jj))
    return res
        

def compute(i, j):
    res = []
    if D[i][j] == "S":
        for di, dj in [(1,0) , (-1,0), (0,1), (0,-1)]: # sve oko njega
            ii, jj = i + di, j + dj
            if not(0 <= ii < n and 0 <= jj < m):
                continue
            if (i,j) in list(neigbours(ii, jj)):
                res.append((di,dj))
        return res
    else: # s obzirom na znak vrati pomake na kojima mora biti cijev npr. za F znamo da mora biti dolje i desno
        res = {
            "|" : [(1,0), (-1,0)],
            "-" : [(0,1), (0,-1)],
            "L" : [(-1,0), (0,1)],
            "J" : [(-1,0), (0,-1)],
            "7" : [(1,0) , (0, -1)],
            "F" : [(1,0) , (0, 1)],
            "." : []
        }[D[i][j]]
        return res

def find_S(lines):
    si, sj = None, None
    for i, line in enumerate(lines):
        if "S" in  line:
            si, sj = i, line.index("S")
            break
    return (si,sj)

def main():
    visited = set()
    distances = {}
    S = find_S(D)
    q = deque([(S, 0)])
    while len(q) > 0:
        print(q)
        top, dist = q.popleft()
        if top in visited:
            continue
        visited.add(top)
        distances[top] = dist

        for nbr in list(neigbours(*top)):
            if nbr in visited:
                continue
            q.append((nbr, dist + 1))
    ans = max(distances.values())
    print(ans)


if __name__ == "__main__":
    main()