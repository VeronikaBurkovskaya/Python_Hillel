"""Написати програму яка поверне кількість введених користувачем слів та загальну кількість символів."""


def count_words(message: str) -> int:
    result = len(message.split(' '))
    return result


message = input("Enter your message")
print(f'Amount of words: {count_words(message)}')
print(f'Amount of symbols: {len(message)}')