from collections import defaultdict, deque
import heapq

input_path = "input.txt"

D = open(input_path, "r").read().split("\n")
G = [[c for c in row] for row in D]

R = len(G)
C = len(G[0])

Q = [(0,0,0,-1,-1)] 
D = {}
while Q:
    dist,r,c,dir,count = heapq.heappop(Q)
    if (r,c,dir,count) in D:
        continue
    D[(r,c,dir,count)] = dist

    for i, (dr,dc) in enumerate([[-1,0],[0,1],[1,0],[0,-1]]):
        rr = r + dr
        cc = c + dc
        new_dir = i
        new_count = (1 if new_dir != dir else count+1)

        not_reverse = ((new_dir + 2) % 4 != dir)
        valid = (new_count <= 3)

        if 0 <= rr < R and 0 <= cc < C and not_reverse and valid:
            cost = int(G[rr][cc])
            heapq.heappush(Q,(dist+cost, rr, cc, new_dir, new_count))
    
ans = 1e9
for (r,c,dir_,indir),v in D.items():
    if r==R-1 and c==C-1:
      ans = min(ans, v)

print(ans)