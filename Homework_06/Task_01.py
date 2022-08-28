"""Дано два кортежі, напишіть функцію яка з'єднає їх в один dict:

  Input:

    coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
    code = ('BTC', 'ETH', 'XRP', 'LTC')
  Output:

    {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}"""


def unite_tuples(first_tuple, second_tuple) -> dict:
    i = 0
    result = {}
    while i < len(first_tuple):
        result[first_tuple[i]] = second_tuple[i]
        i += 1
    return result


coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

print(unite_tuples(coin, code))
