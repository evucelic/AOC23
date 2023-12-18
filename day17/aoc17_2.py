from collections import defaultdict, deque
import math
import heapq # priority queue, min heap

input_path = "input.txt"

D = open(input_path, "r").read().split("\n")
G = [[c for c in row] for row in D]

n = len(G) # len(G) = len(G[0]) = n

def dijkstra(grid):
    D = {}
    queue = [(0, (0,0), -1, -1)]
    directions = [(-1,0), (0,1), (1,0), (0,-1)] # L, D, R, U

    while queue:
        dist, pos, dir, count = heapq.heappop(queue)
        if (pos,dir,count) in D:
            continue
        D[(pos,dir,count)] = dist
        for b, dd in enumerate(directions):
            np = (pos[0] + dd[0], pos[1] + dd[1])
            new_dir = b
            new_count = (1 if new_dir != dir else count + 1)
            reverse_check = ((new_dir + 2) % 4 != dir)
            length_check = (new_count <= 10 and (count == -1 or new_dir == dir or count >= 4)) # krajnja dva slucaja + uvjet 

            if 0 <= np[0] < n and 0 <= np[1] < n and reverse_check and length_check:
                heapq.heappush(queue, (dist+int(grid[np[0]][np[1]]), np, new_dir, new_count))
    
    ans = math.inf
    for (pos,dir,count), dist in D.items():
        if int(pos[0]) == n-1 and int(pos[1]) == n-1:
            ans = min(ans, dist)
    return ans

print(dijkstra(G))