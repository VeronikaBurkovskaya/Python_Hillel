"""1. Дано два списки чисел. Порахуйте кількість чисел які міститься як у першому списку так і у другому. (set)"""


def count_same_numbers(first_list: set, second_list: set) -> int:
    result = first_list.intersection(second_list)
    return len(result)


first = {1, 4, 7, 9, 33, 55, 7, 88, 90}
second = {25, 47, 88, 55, 33, 4, 3, 2, 1}

print(count_same_numbers(first,second))