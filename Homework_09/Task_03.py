"""Написати функцію яка поверне найдовше слово у рядку:

longest_word("What makes a good man") -> makes"""


def longest_word(message: str) -> str:
    word_len = 0
    result = ''
    for word in message.split(' '):
        if len(word) >= word_len:
            result = word
            word_len = len(word)
    return result


print(longest_word("What makes a good man"))
