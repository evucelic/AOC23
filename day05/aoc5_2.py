input_path = "input.txt"


def read_map(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    data = {}
    current_header = None

    for line in lines:
        line = line.strip()

        if line.startswith("seeds:"):
            current_header = "seeds"
            data[current_header] = list(map(int, line.split(": ")[1].split()))
        elif line.endswith("map:"):
            current_header = line.split(" ")[0].lower()
            data[current_header] = []
        elif current_header is not None and line:
            data[current_header].append(list(map(int, line.split())))

    return data


def mapper(R, map_list):
    A = []
    for line in map_list:
        NR = []
        dst = line[0]
        src = line[1]
        rng = line[2]
        while R:
            (st, ed) = R.pop()
            before = (st, min(ed, src))
            inter = (max(st, src), min(src + rng, ed))
            after = (max(src + rng, st), ed)

            if before[1] > before[0]:
                NR.append(before)
            if inter[1] > inter[0]:
                A.append((inter[0] - src + dst, inter[1] - src + dst))
            if after[1] > after[0]:
                NR.append(after)
        # before i after ne upadaju u interval, pošalji ih dalje
        # intervali koji upadaju u range(src, src + rng) idu direktno u rjesenje
        R = NR
    return A + R


def main():
    data = read_map(input_path)
    keys = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]
    P2 = []
    first = data["seeds"]
    pairs = list(zip(first[::2], first[1::2]))

    for st, sz in pairs:
        R = [(st, st + sz)]
        for f in keys:
            R = mapper(R, data[f])
        P2.append(min(R)[0])

    print(min(P2))


if __name__ == "__main__":
    main()
