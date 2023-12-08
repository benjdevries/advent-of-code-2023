import re
from itertools import cycle
from time import sleep


def main():
    nodes = {}
    steps = 0

    with open("input.txt") as f:
        directions = f.readline().strip()
        f.readline()
        for line in f:
            start, left, right = re.findall(r"\w+", line)
            nodes[start] = {"L": left, "R": right, "value": start}

    current_node = nodes["AAA"]
    for direction in cycle(directions):
        print(current_node)
        print("Current step:", steps)
        if current_node["value"] == "ZZZ":
            break

        print(f"Go {direction}")

        current_node = nodes[current_node[direction]]
        steps += 1

    print(f"The solution is {steps}")


if __name__ == "__main__":
    main()
