import re


def get_adjacent_nums(line, start_idx, end_idx) -> list[int]:
    nums = []

    for match in re.finditer(r"\d+", line):
        overlap = range(max(start_idx, match.span()[0]), min(end_idx, match.span()[1]))
        if len(overlap) > 0:
            print(f"adjacent num {match.group()}")
            nums.append(int(match.group()))

    return nums


def get_gear_ratio(
    current_line: str, previous_line: str, next_line: str, gear_idx: int
) -> int:
    """Check if an * is a gear and get its ratio

    *'s are gears if they have two numbers adjacent
    (up, down, left, right, or diagonal) to them.

    The gear ration is the product of multiplying the two adjacent numbers

    :param current_line: The line the * appears in
    :param previous_line: The line above the line the * appears in
    :param next_line: The line below the line the * appears in
    :param gear_idx: The index of ``line`` where the * is located
    :returns: Ration of the gear or 0 if not a gear
    :rtype: int
    """
    # Expand the search to the left and to the right 1 character if
    # the number does not start at the beginning of line or end at the end
    # of the line respectively

    start_idx = gear_idx
    end_idx = gear_idx + 1  # make compatible with range
    if gear_idx > 0:
        start_idx -= 1

    if gear_idx < len(current_line):
        end_idx += 1

    print(previous_line[start_idx:end_idx])
    print(current_line[start_idx:end_idx])
    print(next_line[start_idx:end_idx])

    print("adjacent range", (start_idx, end_idx))

    adjacent_nums = []
    for line in [current_line, previous_line, next_line]:
        adjacent_nums.extend(
            get_adjacent_nums(line, start_idx=start_idx, end_idx=end_idx)
        )

    # If we have 2 adjacent nums, multiply them to get the gear ratio
    if len(adjacent_nums) >= 2:
        return adjacent_nums[0] * adjacent_nums[1]

    return 0


def get_line_total(current_line: str, previous_line: str, next_line: str) -> int:
    """Get all *'s in a line and check if they have a gear ratio"""
    total = 0

    print(f"checking line {current_line}")

    for match in re.finditer(r"\*", current_line):
        print(f"found * at idx {match.start()}")
        ratio = get_gear_ratio(
            current_line=current_line,
            previous_line=previous_line,
            next_line=next_line,
            gear_idx=match.span()[0],
        )
        print("gear ratio", ratio)
        total += ratio
        print()

    return total


def main():
    result = 0

    with open("./input.txt", "r") as f:
        previous_line = None
        current_line = None

        for next_line in f:
            # get rid of \n at end of each line
            next_line = next_line.strip()

            if previous_line is None:
                previous_line = "." * len(next_line)

            if current_line is None:
                current_line = "." * len(next_line)

            result += get_line_total(
                current_line=current_line,
                previous_line=previous_line,
                next_line=next_line,
            )

            previous_line = current_line
            current_line = next_line
            print()

        # Special case for the last line
        result += get_line_total(
            current_line=current_line,
            previous_line=previous_line,
            next_line="." * len(current_line),
        )

    print(f"The solution is {result}")


if __name__ == "__main__":
    main()
