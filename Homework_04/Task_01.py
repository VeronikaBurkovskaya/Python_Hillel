def main():
    x = float(input_value("Enter initial distance"))
    y = float(input_value("Enter final distance"))
    print(f"Days: {count_days(x, y)}")


def count_days(initial_dist: int, final_dist: int):
    days = 0
    while initial_dist <= final_dist:
        initial_dist = initial_dist * 1.1
        days += 1
    return days


def input_value(message: str):
    return input(message)


main()
