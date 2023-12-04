def main():

    result = 0

    with open("./input.txt", "r") as f:
        for line in f.readlines():
            game_header, rounds = line.split(":")

            print(game_header)

            max_for_game = {"red": 0, "green": 0, "blue": 0}

            for r in rounds.split(";"):
                print(r)

                for r_color in r.split(","):
                    count, color = r_color.strip().split(" ")

                    count = int(count)

                    if max_for_game[color] < count:
                        max_for_game[color] = count

            print("color maxes:", max_for_game)

            game_power = max_for_game["red"] * max_for_game["green"] * max_for_game["blue"]
            print("power:", game_power)

            result += game_power

            print("running total of powers: ", result)
            print()

    print(f"The solution is {result}")



if __name__ == "__main__":
    main()
