import numpy as np
input_path = "input.txt"

D = open(input_path, "r").read().split("\n")

G = dict()

for line in D:
    dir, step, color = line.split(" ")
    G[color[1:-1]] = (dir,step)

directions = [(1,0), (0,1), (-1,0), (0,-1)] #RDLU
visited = list()
start = (0,0)
visited.append(start)
length = 0
for key, value in G.items():
    h = key[1:-1]
    dir = "RDLU"[int(key[-1])]
    step = int(h,base=16)

    for i,d in enumerate("RDLU"):
        if dir == d:
            start = (start[0] + int(directions[i][0])*step, start[1] + int(directions[i][1])*step)
            visited.append(start)
            length += step


def shoelace(v_list):
    x_y = np.array(v_list, dtype=np.float64)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    y = x_y[:,1]
    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*abs(S1 - S2)
    return area

total_area = shoelace(visited) + length/2 + 1

print(total_area)