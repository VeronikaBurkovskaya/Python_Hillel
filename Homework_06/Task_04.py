"""Написати функцію, яка повертає поточний час. І обернути її у декоратор

  який відрахує 3 секунди.

  Приклад:

  what_time_is_it_now()
  3
  2
  1
  '16:21'"""
import datetime
import time


def count_second(second: int):
    while second != 0:
        time.sleep(1)
        print(second)
        second -= 1


def what_time_is_it_now(func):
    def wrapped(*args, **kwargs):
        func(*args, **kwargs)

    print(time_now())


def time_now() -> str:
    result = datetime.datetime.now().strftime('%H:%M')
    return result


print("What time is it now?")
what_time_is_it_now(count_second(3))
