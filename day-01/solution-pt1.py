import re


def main():
    total = 0

    with open("input.txt") as f:
        for line in f:
            digits = re.findall(r"\d", line)
            total += int(digits[0] + digits[-1])

    print(f"The solution is {total}")


if __name__ == "__main__":
    main()
