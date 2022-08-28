"""Даний перелік випадкових цілих чисел.
Замініть усі непарні числа списку нулями.
І виведете їхню кількість."""
import random


def change_number_to_null(numbers: list[int]) -> list[int]:
    result = numbers.copy()
    for i, n in enumerate(numbers):
        if n % 2 != 0:
            result[i] = 0
    return result


def count_null_in_list(numbers: list[int]) -> int:
    result = 0
    for i in numbers:
        if i == 0:
            result += 1
    return result


some_list = [1, 5, 6, 7, 122, 344, 5777]

print(change_number_to_null(some_list))
print(count_null_in_list(change_number_to_null(some_list)))
