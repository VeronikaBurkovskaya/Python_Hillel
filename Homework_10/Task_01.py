"""Програма яка при запуску повинна:

Створити текстовий файл, записати в нього дані, які вводить користувач.
Закінченням введення нехай служить порожній текст.
Кожен введений текст у файлі повинен починатися з нового рядка."""


def dataFromUser() -> str:
    message = input("Enter your message")
    result = message
    while message != '':
        message = input("Enter your message")
        result = result + ' ' + message
    return result


def putToFile(func):
    def wrapped(*args, **kwargs):
        func(*args, **kwargs)

    file = open('Text_from_user', 'w')
    file.write(func)
    file.close()


putToFile(dataFromUser())