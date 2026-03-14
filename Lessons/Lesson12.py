def menu_manager():
    menu = {}
    while True:
        print(menu, flush=True)
        match int(input("Выберите действие:\n1. Добавить блюдо\n2. Изменить массу\n")):
            case 1:
                add_dish(menu, input("Введите название:\n"), int(input("Введите массу:\n")))
            case 2:
                change_mass(menu, input("Введите название:\n"), int(input("Введите новую массу:\n")))


def add_dish(menu: dict, name: str, mass: int):
    menu[name] = mass

def change_mass(menu: dict, name:str, new_mass: int):
    menu[name] = new_mass
    del(menu[name])

menu_manager()