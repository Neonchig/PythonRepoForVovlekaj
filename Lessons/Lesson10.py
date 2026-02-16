# def main():
#     Answers = []
#     while True:
        
#         num1 = int(input("Введите первое число:\n"))
#         num2 = int(input("Введите первое число:\n"))
        
#         operation = int(input("Выберите операцию:\n1. Сложение\n2. Умножение\n3. Выход\n"))

#         match operation:
#             case 1:
#                 Answers.append(add(num1, num2))
#                 print(add(num1, num2))
#             case 2:
#                 Answers.append(mul(num1, num2))
#                 print(mul(num1, num2))
#             case 3:
#                 print("Выход...")
#                 return Answers
#             case _:
#                 print("Неверный выбор операции")

# add = lambda num1, num2: num1 + num2

# mul = lambda num1, num2: num1 * num2

# main()

# foo = ["Some_man_0", "Some_man_1", "Some_man_2","Some_man_3"]
# i = 0

# while i < len(foo):
#     print(f"Index: {i}, Name: {foo[i]}")
#     i += 1

# print()

# for index, name in enumerate(foo):
#     print(f"Index: {index}, Name: {name}")

# Код выше дает идентичные результаты

# Так называемая библиотека

class Library():
    
    def __init__(self) -> None:
        self.library = []
    
    def add_book(self, title: str, author: str, created_in: int | None = None):
        if created_in is None:
            self.library.append({"Title": title, "Author": author})
        else:
            self.library.append({"Title": title, "Author": author, "Year of manufacture": created_in})
    
    def remove_book(self, index: int | None):
        if index is int:
            self.library.pop(index)
        else:
            pass

    def get_books(self):
        return self.library
    
def manager(lib: Library):
    while True:
        operation = int(input("Выберите действие:\n1. Добавить книгу\n2. Удалить книгу\n3. Список книг\n4. Выход\n"))
        match operation:
            case 1:
                
                title = input("Введите название книги\n")
                author = input("Введите автора книги\n")
                
                try:
                    created_in_raw = input("Введите год создания\n(Может быть пустым)\n")
                    created_in = int(created_in_raw) if created_in_raw != "" else None
                except:
                    print("Неверный год")
                    created_in = None

                lib.add_book(title, author, created_in)
            
            case 2:
                print()
                for index, book in enumerate(lib.get_books()):
                    print(f"{index}. {book["Title"]} by {book["Author"]}")
                try:
                    deletion = int(input("Введите индекс удаляемой книги\n"))
                except:
                    print("Неверный индекс")
                    deletion = None
                
                lib.remove_book(deletion)

            case 3:
                print()
                for index, book in enumerate(lib.get_books()):
                    print(f"{index}. {book["Title"]} by {book["Author"]}")

            case 4:
                break

main_lib = Library()

manager(main_lib)