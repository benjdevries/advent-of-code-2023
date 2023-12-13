def solve_row(row: list[int]) -> int:
    diffs = [[*row]]

    while any((n != 0 for n in diffs[-1])):
        local_diffs = []
        for a, b in zip(diffs[-1][0:], diffs[-1][1:]):
            local_diffs.append(b - a)
        diffs.append(local_diffs)

    for i in range(len(diffs) - 1, 0, -1):
        diffs[i - 1].append(diffs[i][-1] + diffs[i - 1][-1])

    print(diffs)

    return diffs[0][-1]


def main():
    sequences = []
    total = 0

    with open("input.txt") as f:
        for line in f:
            sequences.append(reversed([int(n) for n in line.split()]))

    for seq in sequences:
        total += solve_row(seq)

    print(f"The solution is {total}")


if __name__ == "__main__":
    main()
