import re


def main():
    with open("input.txt") as f:
        time, dist = f.readlines()

        times = (int(n) for n in re.findall(r"\d+", time))
        distances = (int(n) for n in re.findall(r"\d+", dist))

    total_record_breaks = 1

    for total_time, record in zip(times, distances):
        record_breaks = 0
        for button_push_time in range(0, total_time + 1):
            print(f"button pushed for {button_push_time} ms")
            movement_time = total_time - button_push_time
            print(f"boat ran for {movement_time} ms")
            dist_traveled = movement_time * button_push_time
            print(f"boat traveled {dist_traveled} mm")
            if dist_traveled > record:
                print("New record!")
                record_breaks += 1
            print()

        total_record_breaks *= record_breaks

    print(f"The solution is {total_record_breaks}")


if __name__ == "__main__":
    main()
