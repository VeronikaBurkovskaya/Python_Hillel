"""Написати функцію яка частково приховуватиме e-mail, приклад:

 hide_email(somebody_email@gmail.com) -> em***@**il.com"""


def hide_email(init_email: str) -> str:
    split_message = init_email.split('@')
    part_one = split_message[0]
    part_two = split_message[1]
    result = part_one.replace(part_one[2:(len(part_one))], '**') + '@' + part_two.replace(part_two[:3], '**')
    return result


print(hide_email('somebody_email@gmail.com'))
