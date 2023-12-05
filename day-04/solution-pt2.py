import re


def main():
    with open("./input.txt") as f:
        lines = f.readlines()
        copies = [1] * len(lines)

        for line_num, line in enumerate(lines):
            win_count = 0
            header_and_winning, my_nums = line.split("|")
            my_nums = re.findall(r"\d+", my_nums.strip())
            header, winning_nums = header_and_winning.split(":")
            winning_nums = re.findall(r"\d+", winning_nums.strip())

            print(f"{header} ({copies[line_num]} copies)")

            for num in my_nums:
                if num in winning_nums:
                    win_count += 1

            print(f"{win_count} winning numbers")

            for i in range(line_num + 1, line_num + 1 + win_count):
                copies[i] += copies[line_num]

                print(
                    f"won {copies[line_num]} copies of card {i + 1} ({copies[i]} total)"
                )

            print()

    print(f"The solution is {sum(copies)}")


if __name__ == "__main__":
    main()
