input_path = "input.txt"

D = open(input_path, "r").read().split("\n")
G = [[c for c in row] for row in D]

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

visited = set()
q = [((0, 0), 0)]

height = len(G)
width = len(G[0])


def move(pos, d):
    return ((pos[0] + dir[d][0], pos[1] + dir[d][1]), d)


while q:
    pos, d = q.pop(0)
    if (pos, d) in visited:
        continue
    visited.add((pos, d))

    nxt = []
    current = G[pos[0]][pos[1]]

    if current == ".":
        nxt.append(d)

    elif current == "/":
        nxt.append(3 - d)

    elif current == "\\":
        nxt.append(d + (-1) ** d)

    elif current == "|":
        if d % 2:
            nxt.append(d)
        else:
            nxt.append((d + 1) % 4)
            nxt.append((d + 3) % 4)

    elif current == "-":
        if d % 2:
            nxt.append((d + 1) % 4)
            nxt.append((d + 3) % 4)
        else:
            nxt.append(d)

    for dd in nxt:
        r, c = move(pos, dd)[0]

        if 0 <= r < height and 0 <= c < width and move(pos, dd) not in visited:
            q.append(move(pos, dd))

res = set(pos for pos, _ in visited)
print(len(res))
