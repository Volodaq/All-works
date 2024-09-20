import math


def square(items):
    return math.ceil(items * items)


num_items = float(input("Введите сторону: "))
print(f"площадь: {square(num_items)}")
