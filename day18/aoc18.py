import numpy as np
input_path = "input.txt"

D = open(input_path, "r").read().split("\n")

G = dict()

for line in D:
    dir, step, color = line.split(" ")
    G[color[1:-1]] = (dir,step)

directions = [(-1,0), (0,1), (1,0), (0,-1)]
visited = list()
start = (0,0)
for key, value in G.items():
    dir, step = value
    step = int(step)
    for i,d in enumerate("LDRU"):
        if dir == d:
            for j in range(1,step+1):
                visited.append((start[0] + int(directions[i][0])*j, start[1] + int(directions[i][1]*j)))
            start = (start[0] + int(directions[i][0])*step,start[1] + int(directions[i][1])*step)

def shoelace(v_list):
    x_y = np.array(v_list)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    y = x_y[:,1]
    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)
    return area

total_area = shoelace(visited) + len(visited)/2 + 1

print(total_area)