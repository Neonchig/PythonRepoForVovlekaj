import re
employees = {}

def add_employee(employees_list: dict, full_name: str, age: int, function: str, dep: str, skills: set, salary: int, bonus: int, id: int | None = None) -> None:
    if id is None:
        if len(employees_list) > 0:
            id = max(employees_list) + 1
        elif len(employees_list) == 0:
            id = 0

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

def add_employees_from_file(file_name: str): # ТОЛЬКО ОТЛАДОЧНАЯ ФУНКЦИЯ, НЕ РЕАЛИЗОВАНА ДЛЯ РЕАЛЬНОГО ИСПОЛЬЗОВАНИЯ
    with open(file_name, "r") as file:
        input_strings = file.readlines()
    for i in input_strings:
        out = i.split()
        out = list(map(lambda n: re.sub(r',$', '', n), out))
        add_employee(employees, out[0], int(out[1]), out[2], out[3], set(out[4].replace('[', '').replace(']', '').split(',')), int(out[5]), int(out[6]))

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
        full_info = _employee_info(employees, i)
        summ += full_info['salary'] + full_info['bonus']
    return summ

add_employees_from_file("Homework/test-data.txt")

print(summ_salary(employees))