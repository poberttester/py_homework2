#   Напишите программу банкомат:
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
#   операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


def cash_dispenser():
    bill: float = 0
    count_user_operacions = 0
    operation = ""

    while operation != "выход":

        money_value = float(input("\nВведите сумму: "))
        if bill >= 5000000:
            bill -= (bill * 0.1)
        if money_value % 50 != 0 or money_value == 0:
            print("Введённа сумма должна быть кратна 50, попробуйте ещё раз")
            continue

        operation = input("Введите тип операции: ")

        if operation == "пополнить":
            bill += money_value
            if count_user_operacions == 3:
                bill += bill * 0.03
        elif operation == "снять" and money_value <= bill:
            bill -= money_value
            if 30 >= money_value >= 600:
                bill -= bill * 0.015
            if count_user_operacions == 3:
                bill += bill * 0.03
        elif operation == "снять" and money_value > bill:
            print("На вашем счёте недостаточно средств, попробуйте выполнить другое действие")
            continue
        elif operation == "выход":
            print("Заберите карту")
        else:
            print("Недопустимая операция, попробуйте ещё ввести другие данные")

        # вывод баланса на экран
        print(f"Баланс счёта: {round(bill, 2)}")
