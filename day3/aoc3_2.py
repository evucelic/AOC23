input_path = "input.txt"
P = complex
adj = [P(-1, 1), P(0, 1), P(1, 1), P(-1, 0), P(1, 0), P(-1, -1), P(0, -1), P(1, -1)]

with open(input_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]


def main():
    grid = {}
    symbols = []
    summ = 0

    for y, line in enumerate(lines):
        for x, v in enumerate(line):
            if v != ".":
                grid[P(x, y)] = v
                if v == "*":
                    symbols.append(P(x, y))

    for symbol in symbols:
        parts = getAdj(grid, symbol)
        mul = 1
        if len(parts) == 2:
            for p in parts:
                mul *= p[1]
            summ += mul

    print(summ)
    return None


def getAdj(grid, position):
    parts = set()
    for d in adj:
        parts.add(getNumber(grid, position + d))
    return parts - {None}


def getNumber(grid, position):
    if position not in grid or not grid[position].isnumeric():
        return None

    while position - 1 in grid and grid[position - 1].isnumeric():
        position -= 1

    start = position
    broj = ""

    while position in grid and grid[position].isnumeric():
        broj += grid[position]
        position += 1

    return start, int(broj)


if __name__ == "__main__":
    main()
