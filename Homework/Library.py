class Library():
    
    def __init__(self) -> None:
        self.__library = []
    
    def add_book(self, title: str, author: str, other_info: str, created_in: int | None = None) -> None:
        if created_in is None:
            self.__library.append({"Title": title, "Author": author, "Other_info": other_info})
        else:
            self.__library.append({"Title": title, "Author": author, "Other_info": other_info, "Created_in": created_in})
    
    def remove_book(self, index: int) -> None:
        self.__library.pop(index)

    def clear_library(self) -> None:
        self.__library.clear()

    def get_books(self) -> list[dict]:
        return self.__library.copy()
    
    def get_book_info(self, index: int) -> dict:
        return self.__library[index]

def add_book(lib: Library):
    print('\033c', end="") # Очистка терминала

    title = input("Введите название книги:\n$ ")
    author = input("Введите автора книги:\n$ ")
    other_info = input("Дополнительная информация о книге:\n(Может быть пустым)\n$ ")
    try:
        created_in = int(input("Введите год создания книги:\n(Может быть пустым)\n$ "))
    except:
        print("Неверный формат числа,\nгод не будет установлен")
        created_in = None
    
    lib.add_book(title, author, other_info, created_in)

def print_books_list(lib: Library):
    print('\033c', end="") # Очистка терминала

    books = lib.get_books()
    print(*[f"{index}. {book["Title"]} by {book["Author"]}" for index, book in enumerate(books)], sep="\n")

def print_book_info(lib: Library):
    print('\033c', end="") # Очистка терминала

    print_books_list(lib)
    index = int(input("Введите индекс книги:\n$ "))

    book = lib.get_book_info(index)

    print(f"Книга \"{book["Title"]}\"\nНаписана {book["Author"]} в {book["Created_in"] if book['Created_in'] is not None else "[Не указано]"} году\nДополнительная информация: {book["Other_info"] if book['Other_info'] != "" else "Не указана"}")

def delete_book(lib: Library):
    print('\033c', end="") # Очистка терминала

    print_books_list(lib)
    try:
        index = int(input("Введите индекс книги или exit для выхода:\n$ "))
        lib.remove_book(index)
    except:
        pass

def clear_lib(lib: Library):
    print('\033c', end="") # Очистка терминала

    choice = input("Вы хотите очистить библиотеку? (y/N):\n$ ")

    if choice.lower() == "y":
        lib.clear_library()
    else:
        pass

def lib_manager(lib: Library):
    while True:
        try:
            print('\033c', end="") # Очистка терминала
            option = int(input("Выберите действие:\n1. Добавить книгу\n2. Список книг\n3. Показать инфорамцию о книге\n4. Удалить книгу\n5. Очистить библиотеку\n6. Выход\n$ "))

            match option:
                case 1:
                    add_book(lib)
                case 2:
                    print_books_list(lib)
                    input("Enter для продолжения\n") # Чтобы пользователь увидел сообщение
                case 3:
                    try:
                        print_book_info(lib)
                    except IndexError:
                        print("Ошибка.\nКниги не существует")
                    input("Enter для продолжения\n") # Чтобы пользователь увидел сообщение
                case 4:
                    delete_book(lib)
                case 5:
                    clear_lib(lib)
                case 6:
                    print("Выход...")
                    break
                case _:
                    print("Неверный выбор")
                    input("Enter для продолжения\n") # Чтобы пользователь увидел сообщение
        except ValueError:
            print("Неверный формат числа")
            input("Enter для продолжения\n") # Чтобы пользователь увидел сообщение
        except KeyboardInterrupt:
            print("Выход...")
            break

if __name__ == "__main__":    
    main_lib = Library()
    
    lib_manager(main_lib)