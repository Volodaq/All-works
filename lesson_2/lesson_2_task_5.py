def month_to_season(month):
    if 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    elif 11 <= month or month == 1 or month == 2:
        return "Зима"
    else:
        return "Неверный номер месяца"


try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month))

except ValueError:
    print("Введите целое число от 1 до 12.")
