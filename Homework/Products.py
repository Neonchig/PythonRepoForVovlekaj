def show_cart(cart: dict) -> list:
    return list(f"{str(item)} -- {str(cart[item])}" for item in cart)

def show_items(cart: dict) -> list:
    return list(item for item in cart)

def add_item(cart: dict, item:str, price: float) -> bool:
    if price > 0 and len(item) > 0:
        cart[item] = price
        return True
    else:
        return False

def remove_item(cart: dict, item: str) -> bool:
    if item in cart:
        cart.pop(item)
        return True
    else:
        return False
    
def change_price(cart: dict, item: str, new_price: float) -> bool:
    if item not in show_items(cart):
        return False
    
    cart[item] = new_price

def main():
    cart = {}
    while True:
        print('\033c{')
        print(*list(show_cart(cart)), sep='\n')
        print('}')
        select = int(input("Выберите действие:\n1. Добавить товар\n2. Удалить товар\n3. Изменить товар\n$ "))
        match select:
            case 1:
                print('\033c')
                print(*list(str(i + 1) + "." + " " + show_cart(cart)[i] for i in range(len(show_cart(cart)))), sep='\n')
                add_item(cart = cart, item = input("Введите название товара:\n"), price = int(input("Введите цену:\n")))
            case 2:
                print('\033c')
                print(*list(str(i + 1) + "." + " " + show_cart(cart)[i] for i in range(len(show_cart(cart)))), sep='\n')
                remove_item(cart = cart, item = show_items(cart)[int(input("Введите номер удаляемого товара:\n")) - 1])
            case 3:
                print('\033c')
                print(*list(str(i + 1) + "." + " " + show_cart(cart)[i] for i in range(len(show_cart(cart)))), sep='\n')
                change_price(cart = cart, item = show_items(cart)[int(input("Введите номер изменяемого товара:\n")) - 1], new_price = float(input("Введите новую цену:\n")))
        
main()