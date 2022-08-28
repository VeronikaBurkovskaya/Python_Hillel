"""Дано перелік значень. Повернути словник, де кожен ключ - це індекс листа,

  а значення листа – це значення ключа:

  Input:

    ['a', 'b', 'c', 'd', 'e']
  Output

  {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}"""


def list_to_dict(init_tuple) -> dict:
    i = 0
    result = {}
    while i < len(init_tuple):
        result[i] = init_tuple[i]
        i += 1
    return result


some_tuple =['a', 'b', 'c', 'd', 'e']
print(list_to_dict(some_tuple))