"""Написати функцію яка замінить у тексті слово інше.

 Функція приймає 4 аргументи, початковий рядок, слово, що замінюється, нове слово, кількість замін, приклад:



 fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1)
 -> 'Marvel makes good movies, DC makes good comics'

 fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2)
 -> 'Marvel makes good movies, Marvel makes good comics'"""


def fake_string(message: str, old_word: str, new_word, count_changes: int) -> str:
    return message.replace(old_word, new_word, count_changes)


print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1))

print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2))
