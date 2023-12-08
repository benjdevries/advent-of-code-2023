import re


def get_next_id(
    input_id: int, maps: list[tuple[int, int, int]]
) -> tuple[int, int, int]:
    """Get the next id from a map range

    Falls back to the same input_id if no range matches
    """

    for m in maps:
        dest_start, source_start, map_range = m

        if source_start <= input_id < source_start + map_range:
            offset = input_id - source_start
            output = dest_start + offset
            # print(f"mapped to {output}")

            return m

    # print("no valid map, falling back to input")
    return input_id, input_id, 1


def map_to_next_range(input_ranges, map_ranges):
    for i_range in input_ranges:
        print("destination start", i_range[0])
        print("source start", i_range[1])
        print("range span", i_range[2])

        output_range = get_next_id(i_range[0], map_ranges)

        output_offset = i_range[0]

        print("output range", output_range)


def main():
    maps = {}
    min_location = 999_999_999_999
    sorted_seeds = []

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
                dest, source, n = (int(x) for x in line.strip().split())
                maps[current_map].append(tuple())

    for i in range(0, len(seeds), 2):
        sorted_seeds.append((seeds[i], seeds[i] + seeds[1]))
    sorted_seeds.sort()
    print(sorted_seeds)
    source_ranges = sorted_seeds

    # for m, vals in maps.items():
    #     vals.sort(key=lambda x: x[1])
    #     print(m, vals)
    #     next_range = map_to_next_range(input_ranges=source_ranges, map_ranges=vals)
    #     break
    # map_vals = maps[m]

    # for i in range(0, len(seeds), 2):
    #     # iterate in pairs
    #     start_id = seeds[i]
    #     count = seeds[i + 1]
    #
    #     for seed in range(start_id, start_id + count):
    #         next_id = seed
    #         for m in maps:
    #             # print(m)
    #             next_id = get_next_id(next_id, maps[m])
    #
    #         if next_id < min_location:
    #             min_location = next_id
    #             print(f"new smallest location {min_location}")
    #         # print()
    #
    # print(f"The solution is {min}")


if __name__ == "__main__":
    main()
