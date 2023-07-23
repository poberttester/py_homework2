# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction


def operations_with_fractions(string_1="51/71", string_2="124/136"):
    numbers_1 = string_1.split("/")
    numerator_1 = int(numbers_1[0])
    denominator_1 = int(numbers_1[1])

    numbers_2 = string_2.split("/")
    numerator_2 = int(numbers_2[0])
    denominator_2 = int(numbers_2[1])

    # сумма дробей.
    sum_numerator = (numerator_1 * denominator_2 + numerator_2 * denominator_1)
    sum_denominator = denominator_1 * denominator_2

    if sum_numerator > sum_denominator:
        smaller = sum_denominator
    else:
        smaller = sum_numerator

    for i in range(1, smaller + 1):
        if (sum_numerator % i == 0) and (sum_denominator % i == 0):
            greatest_common_divisor = i

    print(f'\nСумма: {sum_numerator // greatest_common_divisor}/{sum_denominator // greatest_common_divisor}')

    # произведение дробей.
    multi_numerator = numerator_1 * numerator_2
    multi_denominator = denominator_1 * denominator_2

    if multi_numerator > multi_denominator:
        smaller = multi_denominator
    else:
        smaller = multi_numerator

    for i in range(1, smaller + 1):
        if (multi_numerator % i == 0) and (multi_denominator % i == 0):
            greatest_common_divisor = i

    print(f'Произведение: {multi_numerator // greatest_common_divisor}/{multi_denominator // greatest_common_divisor}')

    # проверка правильности вычислений при помощи модуля fractions.
    a = Fraction(numerator_1, denominator_1)
    b = Fraction(numerator_2, denominator_2)

    print(f'Проверка суммы: {a + b}')
    print(f'Проверка произведения: {a * b}')
