"""Написати функцію square, що приймає 1 аргумент - сторону квадрата,
і повертає 3 значення (за допомогою кортежу):
периметр квадрата, площа квадрата та діагональ квадрата."""
import math


def square(size: int) -> tuple[int, int, int]:
    perimeter = 4 * size
    area = size * size
    dioalog = size * math.sqrt(2)
    return perimeter, area, dioalog


print(square(5))
