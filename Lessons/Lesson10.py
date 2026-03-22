"""
def main():
    Answers = []
    while True:
        
        num1 = int(input("Введите первое число:\n"))
        num2 = int(input("Введите первое число:\n"))
        
        operation = int(input("Выберите операцию:\n1. Сложение\n2. Умножение\n3. Выход\n"))

        match operation:
            case 1:
                Answers.append(add(num1, num2))
                print(add(num1, num2))
            case 2:
                Answers.append(mul(num1, num2))
                print(mul(num1, num2))
            case 3:
                print("Выход...")
                return Answers
            case _:
                print("Неверный выбор операции")

add = lambda num1, num2: num1 + num2

mul = lambda num1, num2: num1 * num2

main()

Калькулятор для 2-х действий

"""

"""
foo = ["Some_man_0", "Some_man_1", "Some_man_2","Some_man_3"]
i = 0

while i < len(foo):
    print(f"Index: {i}, Name: {foo[i]}")
    i += 1

print()

for index, name in enumerate(foo):
    print(f"Index: {index}, Name: {name}")

Код выше дает идентичные результаты
"""