import re


def parse_int_from_word(digit_or_word):
    try:
        return int(digit_or_word)

    except ValueError:
        match digit_or_word:
            case "one":
                return 1
            case "two":
                return 2
            case "three":
                return 3
            case "four":
                return 4
            case "five":
                return 5
            case "six":
                return 6
            case "seven":
                return 7
            case "eight":
                return 8
            case "nine":
                return 9


def main():

    nums = []

    with open("./input.txt", "r") as f:
        for line in f:
            print(f"parsing {line[0:-1]}")
            # Need to use a positive lookahead here because cases like "eighthree"
            # should be parsed as 83 even though the 't' is shared.
            digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
            print(f"found {digits}")

            first = parse_int_from_word(digits[0])
            last = parse_int_from_word(digits[-1])

            parsed = int(str(first) + str(last))
            print(f"parsed {parsed}")

            nums.append(parsed)
            print()

    print(f"The solution is {sum(nums)}")


if __name__ == "__main__":
    main()
