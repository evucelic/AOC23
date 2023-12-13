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


def mapper(element, map_list):
    candidates = {seed: seed for seed in element}
    for seed in element:
        for line in map_list:
            destination = line[0]
            source = line[1]
            rng = line[2]
            if source <= seed < source + rng:
                mapping = destination + seed - source
                candidates.update({seed: mapping})
    return candidates


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
    location = dict()
    first = data["seeds"]
    for i, key in enumerate(keys):
        if i < len(data):
            location = mapper(first, data[key])
            first = location.values()

    print(min(location.values()))


if __name__ == "__main__":
    main()
