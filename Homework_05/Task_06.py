"""6. * Написати функцію яка прибере з dict елементи із значеннями None:
  {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
  Повинно повернути {'first_color': 'Red', 'second_color': 'Green'} # * dict може бути довільним"""


def remove_none(dictionary: dict) -> dict:
    result = dictionary.copy()
    for key, value in dictionary.items():
        if value is None:
            del result[key]
            break
    return result


intial_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}

print(remove_none(intial_dict))
