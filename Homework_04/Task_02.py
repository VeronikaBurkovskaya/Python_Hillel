def ask_numbers():
    number = 1
    result = list()
    while number > 0:
        number = int(input("Enter your number"))
        result.append(number)
    result.remove(0)
    return result


def count_num(numbers: list()):
    return len(numbers)


def sum_num(numbers: list()):
    result = 0
    for i in numbers:
        result += i
    return result


def multiplicatio_num(numbers: list()):
    result = 1
    for i in numbers:
        result = result * i
    return result


def max_number(numbers: list()):
    max_value = max(numbers)
    i = 0
    index_max = 0
    while i < len(numbers):
        if numbers[i] == max_value:
            index_max = i
        i += 1
    return max_value, index_max


def number_type(numbers: list()):
    even = 0
    not_even = 0
    for i in numbers:
        if i % 2 == 0:
            even += 1
        else:
            not_even += 1
    return even, not_even


def equal_max(numbers: list()):
    result = 0
    for i in numbers:
        if i == max_number(numbers)[0]:
            result += 1
    return result


def second_max(numbers: list()):
    max_value = max_number(numbers)[0]
    update_list = numbers.remove(max_value)
    second_value = max(update_list)
    return second_value


def main():
    from_user = ask_numbers()
    print(from_user)
    print(f"Count numbers: {count_num(from_user)}")
    print(f"Sum: {sum_num(from_user)}")
    print(f"Multiplication: {multiplicatio_num(from_user)}")
    print(f"Avarage: {sum_num(from_user) / count_num(from_user)}")
    print(f"Max value {max_number(from_user)[0]} Index {max_number(from_user)[1]}")
    print(f"Count of even numbers {number_type(from_user)[0]}")
    print(f"Count of not even numbers {number_type(from_user)[1]}")
    print(second_max(from_user))

main()
