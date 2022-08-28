"""Написати калькулятор температури.

    Користувач вводить число та тип температури (C, F, K - Цельсій, Фарренгейт, Кельвін відповідно)

    Програма має вивести температуру у трьох шкалах температур – Цельсій, Фарренгейт, Кельвін."""


def tem_celsius(temperature: float, type: str) -> float:
    match type:
        case "C":
            return temperature
        case "F":
            return (temperature - 32) * (5 / 9)
        case "K":
            return temperature - 273


def tem_kelvin(temperature: float, type: str) -> float:
    match type:
        case "C":
            return temperature + 273
        case "F":
            return ((temperature - 32) * (5 / 9)) + 273
        case "K":
            return temperature


def tem_faringate(temperature: float, type: str) -> float:
    match type:
        case "C":
            return ((temperature * (5 / 9)) +32)
        case "F":
            return temperature
        case "K":
            return ((temperature - 273) * (9 / 5)) + 32


def tem_summary(temperature: float, type:str) -> tuple[float,float,float]:
    return tem_celsius(temperature,type),tem_kelvin(temperature,type),tem_faringate(temperature,type)


temperature = float(input("Enter your temperature"))
type_tem = input("Enter your type")
result = tem_summary(temperature,type_tem)

print(f'Temperature on Celsius: {result[0]}')
print(f'Temperature on Kelvin: {result[1]}')
print(f'Temperature on Faringate: {result[2]}')