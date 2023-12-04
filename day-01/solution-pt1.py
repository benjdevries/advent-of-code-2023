import re


def main():

    nums = []

    with open("./input.txt", "r") as f:
        for line in f.readlines():
            digits = re.findall(r'\d', line)
            nums.append(int(digits[0] + digits[-1]))

    print(f"The solution is {sum(nums)}")


if __name__ == "__main__":
    main()
