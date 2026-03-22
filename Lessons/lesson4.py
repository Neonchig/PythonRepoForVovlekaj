# def recursion(i = 0) -> None:
#     def iteration(i = i):
#         i += 1
#         recursion(i)
#         print(i)
#     if i < 10:
#         iteration()
#     else:
#         return True
    
# recursion()

def main():
    func_list = ["1. Сумма", "2. Разность", "3. Умножение", "4. Деление", "5. Степень", "6. Выход"]
    while True:
        print("Выберите номер функции")
        print(*func_list, sep="\n")
        func_number = int(input())
        if func_number != 6:
            num1 = int(input("Введите 1 число\n"))
            num2 = int(input("Введите 2 число\n"))
        match func_number:
            case 1:
                print("Ответ: ", add(num1, num2))
            case 2:
                print("Ответ: ", sub(num1, num2))
            case 3:
                print("Ответ: ", mul(num1, num2))
            case 4:
                print("Ответ: ", div(num1, num2))
            case 5:
                print("Ответ: ", power(num1, num2))
            case 6:
                print("Выход...")
                break


def add(num1:float, num2:float) -> float:
    return (num1 + num2)

def sub(num1:float, num2:float) -> float:
    return (num1 - num2)

def mul(num1:float, num2:float) -> float:
    return (num1 * num2)

def div(num1: float, num2:float) -> float:
    return (num1 / num2)

def power(num1: float, num2: float) -> float:
    return (num1 ** num2)

main()