"""Написати функцію, яка визначить, чи є введений текст паліндромом
(той який читається однаково з будь-якого боку), приклад:

Шалаш, зараз, Дід, Піп, 13231
Паліндром — і ні морд, ні лап"""

def getTextFromUser() -> str:
    message = input("Enter your text").lower()
    result = message.split()
    return result


def isPolindrom(func: str) -> bool:
    def wrapped(*args, **kwargs):
        func(*args, **kwargs)

    original_word = list(func)
    reversed_word = original_word.copy()
    reversed_word.reverse()
    if original_word == reversed_word:
        return True
    else:
        return False


print(isPolindrom(getTextFromUser()))
