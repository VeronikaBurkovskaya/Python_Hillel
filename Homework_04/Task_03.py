def input_value(message: str):
    return input(message)


def range_a_b(a: int, b: int):
    if a < b:
        result = list (range(a, b+1))
    else:
        result = list (range(b, a+1))
        result.reverse()
    return result


def main():
    x = int(input_value("Enter A"))
    y = int(input_value("Enter B"))
    print(range_a_b(x,y))

main()


