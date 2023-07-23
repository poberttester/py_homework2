# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def to_hex_convert(number: int, n: int = 16):
    hex_number = ''
    hex_collection = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']

    while number != 0:
        index = number % n
        result = str(hex_collection[index])
        hex_number = result + hex_number
        number //= n

    return hex_number


def hexadecimal_output():
    number: int = int(input("\nВведите число: "))
    print(f"В шестнадцатиричной системе: {to_hex_convert(number)}")
    print(f"Проверка: {hex(number)[2:]}")
