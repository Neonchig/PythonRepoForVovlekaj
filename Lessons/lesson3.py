str1 = 0
str2 = 0
while True:
    try:
        str1 = input("Введите первое число или exit для выхода:\n")
        num1 = int(str1)
        str2 = input("Введите второе число или exit для выхода:\n")
        num2 = int(str2)
        print(num1 + num2)
    except:
        if str1 == "exit" or str2 == "exit":
            print("Выход...")
            break
        else:
            print("Неверный формат чисел")