"""Написати функцію яка зрушить отриманий список на N елементів
вправо або вліво, аргументи, що приймаються - список і натуральне число
(якщо негативне зрушуємо вліво, позитивне - вправо)."""


def moveList(initial_list, moveTo: int) -> list:
    new_list = initial_list.copy()
    new_list = new_list[moveTo:] + new_list[:moveTo]
    return new_list


some_list = [1, 2, 3, 4, 5]
print(moveList(some_list, -2))
