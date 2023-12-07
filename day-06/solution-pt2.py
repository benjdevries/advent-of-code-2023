import re


def find_boundary(time: int, record: int) -> int:
    """Find the shortest button press that beats the record

    Implements a simple binary search over the lower half of
    the possible time values.
    """
    start = 0
    end = time // 2
    press_time = 0
    dist_traveled = 0

    while start <= end:
        press_time = (start + end) // 2

        dist_traveled = (time - press_time) * press_time

        if dist_traveled < record:
            start = press_time + 1

        elif dist_traveled > record:
            end = press_time - 1

        else:
            return press_time

    # We didn't find an exact boundary. If we're still below the record,
    # bump the press time up 1 ms to get over the record,
    # else we are already as close as we can get, so return the current val.
    if dist_traveled < record:
        press_time += 1

    return press_time


def main():
    with open("input.txt") as f:
        time, record = f.readlines()
        time = int("".join(re.findall(r"\d+", time)))
        record = int("".join(re.findall(r"\d+", record)))

    # First, find the shortest press time that beats the record
    lower_boundary = find_boundary(time, record)
    print(f"lower boundary {lower_boundary}")

    # The problem is symetric since multiplication is commutative
    upper_boundary = time - lower_boundary
    print(f"upper boundary {upper_boundary}")

    print(f"The solution is {upper_boundary - lower_boundary + 1}")


if __name__ == "__main__":
    main()
