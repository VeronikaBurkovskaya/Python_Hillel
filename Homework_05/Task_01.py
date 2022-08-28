"""Написати функцію `is_prime`, що приймає 1 аргумент - число від 0 до 1000,
 і повертає `True`, якщо воно просте, і `False` - інакше."""


def is_prime_number(number: int):
    for i in list(range(2, number)):
        if number % i == 0:
            return False
    return True


number_check = int(input("Enter number"))
print(f'Number {number_check} is prime: {is_prime_number(number_check)}')


