def input_value(message: str):
    return input(message)


def stairs(number: int):
    i = 1
    while i <= number:
        for k in range(1, i+1):
            print(k, end="")
        i += 1
        print("")


def main():
    x = int(input_value("Enter A"))
    stairs(x)

main()