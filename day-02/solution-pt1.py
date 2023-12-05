def main():
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    result = 0

    with open("./input.txt", "r") as f:
        for line in f:
            game_header, rounds = line.split(":")

            print(game_header)
            game_id = int(game_header.split(" ")[1])
            game_is_valid = True

            for r in rounds.split(";"):
                print(r)

                drawn = {"red": 0, "green": 0, "blue": 0}

                for r_color in r.split(","):
                    count, color = r_color.strip().split(" ")
                    drawn[color] = int(count)

                print(drawn)

                is_possible = (
                    (drawn["red"] <= MAX_RED)
                    and (drawn["green"] <= MAX_GREEN)
                    and (drawn["blue"] <= MAX_BLUE)
                )
                print("is possible?", is_possible)

                if not is_possible:
                    game_is_valid = False

            print("valid game?", game_is_valid)

            if game_is_valid:
                result += game_id

            print("running total of valid game IDs: ", result)
            print()

    print(f"The solution is {result}")


if __name__ == "__main__":
    main()
