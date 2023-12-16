input_path = "input.txt"

D = open(input_path, "r").read().split("\n")
G = [[c for c in row] for row in D]
start = (0, 0)
d = 0
h = len(G)
w = len(G[0])
res = []

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # R, D, L, U

def move(pos, d):
    return ((pos[0] + dir[d][0], pos[1] + dir[d][1]), d)

def FUNC(start, init_d):
    q = [(start, init_d)]
    visited = set()

    while q:
        pos, d = q.pop(0)

        if (pos, d) in visited:
            continue
        visited.add((pos, d))

        _next_d = []
        curr = G[pos[0]][pos[1]]

        if curr == ".":
            _next_d.append(d)
        elif curr == "\\":
            _next_d.append(d + (-1) ** d)
        elif curr == "/":
            _next_d.append(3 - d)
        elif curr == "-":
            if d % 2:
                _next_d.append((d + 1) % 4)
                _next_d.append((d + 3) % 4)
            else:
                _next_d.append(d)
        elif curr == "|":
            if d % 2:
                _next_d.append(d)
            else:
                _next_d.append((d + 1) % 4)
                _next_d.append((d + 3) % 4)

        for dd in _next_d:
            r, c = move(pos, dd)[0]

            if 0 <= r < h and 0 <= c < w and move(pos, dd) not in visited:
                q.append(move(pos, dd))

    return len(set(pos for pos, _ in visited))

for y in range(h):
    for x in range(w):
        if y not in [0, h - 1] and x not in [0, w - 1]:
            continue

        init_d = []

        if y == 0:
            init_d.append(1)
        elif y == h - 1:
            init_d.append(3)

        if x == 0:
            init_d.append(0)
        elif x == w - 1:
            init_d.append(2)

        for d in init_d:
            res.append(FUNC((y, x), d))

print(max(res))