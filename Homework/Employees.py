import re


def add_employee(employees_list: dict, full_name: str, age: int, function: str, dep: str, skills: set, salary: int, bonus: int, id: int | str = "") -> None:
    if id == "":
        if len(employees_list) > 0:
            id = max(employees_list) + 1
        elif len(employees_list) == 0:
            id = 0
    if id in employees_list or id is str:
        raise KeyError
    employees_list[id] = {
        "personal": {
            "full_name": full_name, 
            "age": age
        }, 
        "proffessional": {
            "function": function, 
            "departament": dep,
            "skills": skills
        }, 
        "financial": {
            "salary": salary, 
            "bonus": bonus
        }
    }

def add_employees_from_file(employee_list: dict, file_name: str): # ТОЛЬКО ОТЛАДОЧНАЯ ФУНКЦИЯ, НЕ РЕАЛИЗОВАНА ДЛЯ РЕАЛЬНОГО ИСПОЛЬЗОВАНИЯ
    with open(file_name, "r") as file:
        input_strings = file.readlines()
    for i in input_strings:
        out = i.split()
        out = list(map(lambda n: re.sub(r',$', '', n), out))
        add_employee(employee_list, out[0], int(out[1]), out[2], out[3], set(out[4].replace('[', '').replace(']', '').split(',')), int(out[5]), int(out[6]))

def _list_employees(employees_list: dict) -> list:
    return [{id: employees_list[id]["personal"]["full_name"]} for id in employees_list]

def _employee_info(employees_list: dict, id: int) -> dict:
    return {"id": id, "name": employees_list[id]["personal"]["full_name"], "age": employees_list[id]["personal"]["age"], 
            "function": employees_list[id]["proffessional"]["function"], "departament": employees_list[id]["proffessional"]["departament"], "skills": employees_list[id]["proffessional"]["skills"],
            "salary": employees_list[id]["financial"]["salary"], "bonus": employees_list[id]["financial"]["bonus"]}

def list_employees(employees_list: dict):
    all_employees = _list_employees(employees_list)
    for i in all_employees:
        for j in i:
            print(f"{j}. {i[j]}")

def check_skills(employees_list: dict, skills: set):
    output = []
    for i in employees_list:
        full_info = _employee_info(employees_list, i)
        if skills.issubset(full_info["skills"]):
            output.append(i)
    return output

def employee_info(employees_list: dict, id: int):
    full_info = _employee_info(employees_list, id)
    print(f"Карточка сотрудника №{id}\nПолное имя - {full_info["name"]}\nВозраст сотрудника - {full_info["age"]}\nДолжность сотрудника - {full_info["function"]}\nОтдел работы сотрудника - {full_info["departament"]}\nНавыки сотрудника - {full_info['skills']}\nБазовая зарплата сотрудника - {full_info["salary"]}\nБонус сотрудника - {full_info["bonus"]}")

def change_salary(employees_list: dict, id: int, new_salary: int):
    employees_list[id]["financial"]["salary"] = new_salary

def change_bonus(employees_list: dict, id: int, new_bonus: int):
    employees_list[id]["financial"]["bonus"] = new_bonus

def add_skill(employees_list: dict, id: int, skill: str):
    employees_list[id]["proffessional"]["skills"].add(skill)

def delete_employee(employee_list: dict, id: int):
    employee_list.pop(id)

def summ_salary(employee_list: dict):
    summ = 0
    for i in employee_list:
        full_info = _employee_info(employee_list, i)
        summ += full_info['salary'] + full_info['bonus']
    return summ


def main():
    employees = {}
    running = True
    add_employees_from_file(employees, "Homework/test-data.txt")
    while running:
        try:
            var = int(input("Меню:\n[1] Добавить сотрудника\n[2] Список сотрудников\n[3] Изменить информацию о сотруднике\n[4] Удалить сотрудника\n[5] Выполнить поиск навыков\n[0] Выход"))
        except:
            print("Неверный ввод")
            var = 8
        match var:
            case 1:
                try:
                    add_employee(employees, input("Введите полное имя сотрудника: "), int(input("Введите возраст сотрудника: ")), input("Введите должность сотрудника: "), input("Введите отдел, в котором работает сотрудник"), set(input("Введите навыки сотрудника через запятую без пробелов").split(',')), int(input("Введите зарплату сотрудника: ")), int(input("Введите бонус к зарплате сотрудника: ")), "Введите идентификатор сотрудника или оставьте пустым для автоматического выбора: ")
                except:
                    print('Неверный ввод')
            case 2:
                list_employees(employees)
            case 3:
                try:
                    answ = int(input("Что именно вы хотите изменить?\n[1] Зарплата сотрудника\n[2] Бонус сотрудника\n[3] Добавить навык сотруднику\n"))
                except:
                    print('Неверный ввод')
                    answ = 0
                match answ:
                    case 1:
                        try:
                            change_salary(employees, int(input("Введите идентификатор сотрудника: ")), int(input("Введите новую зарплату сотрудника: ")))
                        except:
                            print('Неверный ввод')
                    case 2:
                        try:
                            change_bonus(employees, int(input("Введите идентификатор сотрудника: ")), int(input("Введите новый бонус сотрудника: ")))
                        except:
                            print('Неверный ввод')
                    case 3:
                        try:
                            add_skill(employees, int(input("Введите идентификатор сотрудника: ")), input("Введите новый навык сотрудника: "))
                        except:
                            print('Неверный ввод')
                    case _:
                        pass
            case 4:
                try:
                    delete_employee(employees, int(input("Введите идентификатор сотрудника: ")))
                except:
                    print('Неверный ввод')
            case 5:
                check_skills(employees, set(input("Перечислите искомые навыки через запятую без пробелов: ").split(',')))
            case 0:
                print('Выход...')
                running = False
            case _:
                pass

main()