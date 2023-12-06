import re


def get_next_id(input_id: int, maps: list[list[int, int, int]]) -> int:
    """Get the next id from a map range

    Falls back to the same input_id if no range matches
    """

    for m in maps:
        dest_start, source_start, map_range = m

        if source_start <= input_id < source_start + map_range:
            offset = input_id - source_start
            output = dest_start + offset
            print(f"mapped to {output}")

            return output

    print("no valid map, falling back to input")
    return input_id


def main():
    maps = {}
    locations = []

    with open("./input.txt") as f:
        seeds = [int(n) for n in re.findall(r"\d+", f.readline())]

        current_map = ""

        for line in f:
            if line == "\n":
                continue

            elif line[0].isalpha():
                current_map = line.split()[0]
                maps[current_map] = []

            elif line[0].isdigit():
                maps[current_map].append([int(n) for n in line.strip().split()])

    for seed in seeds:
        print(f"mapping seed {seed}")
        next_id = seed
        for m in maps:
            print(m)
            next_id = get_next_id(next_id, maps[m])

        print(f"seed {seed} maps to location {next_id}")
        locations.append(next_id)
        print()

    print(f"The solution is {min(locations)}")


if __name__ == "__main__":
    main()
