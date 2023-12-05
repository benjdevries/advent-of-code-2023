import re


def is_symbol(char: str) -> bool:
    """A character is a symbol if it is not a digit or a period"""
    return not char.isdigit() and not char == "."


def check_has_symbol(
    current_line: str, previous_line: str, next_line: str, start_idx: int, end_idx: int
) -> bool:
    """Check if a number has an adjacent symbol

    Could be to the left or right, or in the row above or below +/- 1 index (diagonal)
    :param current_line: The line the number appears in
    :param previous_line: The line above the line the number appears in
    :param next_line: The line below the line the number appears in
    :param start_idx: The index of ``line`` where the number starts
    :param end_idx: The index of ``line`` where the number ends
    :returns: Whether the number has an adjacent symbol
    :rtype: bool
    """
    # Expand the search to the left and to the right 1 character if
    # the number does not start at the beginning of line or end at the end
    # of the line respectively
    if start_idx > 0:
        start_idx -= 1

    if end_idx < len(current_line):
        end_idx += 1

    print(previous_line[start_idx:end_idx])
    print(current_line[start_idx:end_idx])
    print(next_line[start_idx:end_idx])

    for i in range(start_idx, end_idx):
        if (
            is_symbol(current_line[i])
            or is_symbol(previous_line[i])
            or is_symbol(next_line[i])
        ):
            return True

    return False


def get_line_total(current_line: str, previous_line: str, next_line: str) -> int:
    total = 0

    print(f"checking line {current_line}")

    for match in re.finditer(r"\d+", current_line):
        print(f"found {match.group()} spanning {match.span()}")
        is_part_num = check_has_symbol(
            current_line=current_line,
            previous_line=previous_line,
            next_line=next_line,
            start_idx=match.span()[0],
            end_idx=match.span()[1],
        )
        print("is part number?", is_part_num)
        if is_part_num:
            total += int(match.group())
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
