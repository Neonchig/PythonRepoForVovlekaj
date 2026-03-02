user_input = input("Введите элементы списка через пробел\n").split()
user_input = list(map(lambda x: int(x), user_input))

print(f"Список четных элементов: {list(filter(lambda x: x % 2 == 0, user_input))}")
print(f"Список нечетных элементов: {list(filter(lambda x: x % 2 != 0, user_input))}")
print(f"Преобразованные числа: {list(map(abs, user_input))}")