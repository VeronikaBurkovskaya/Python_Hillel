def input_value(message: str):
    return input(message)


def main():
    some_str = str(input_value("Enter message"))
    print(some_str[3])
    print(some_str[-2])
    print(some_str[0:5])
    print(some_str[0:(len(some_str)-2)])
    print(some_str[0:(len(some_str)):2])
    print(some_str[1:(len(some_str)):2])
    print(some_str[::-1])
    print(some_str[-2::-2])
    print(len(some_str))


main()