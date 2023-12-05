import re


def main():
    total = 0

    with open("./input.txt") as f:
        for line in f:
            win_count = 0
            header_and_winning, my_nums = line.split("|")
            my_nums = re.findall(r"\d+", my_nums.strip())
            print("my nums", my_nums)
            header, winning_nums = header_and_winning.split(":")
            winning_nums = re.findall(r"\d+", winning_nums.strip())
            print("winning nums", winning_nums)

            print(header)

            for num in my_nums:
                if num in winning_nums:
                    print(f"{num} wins!")
                    win_count += 1

            # Worth 1pt for 1 win (2^0) and doubled for every win after that
            line_val = 2 ** (win_count - 1) if win_count else 0

            print(f"found {win_count} winning numbers for a value of {line_val}")
            total += line_val
            print()

    print(f"The solution is {total}")


if __name__ == "__main__":
    main()
