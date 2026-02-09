def parent_function():
    i = 0
    def my_func():
        nonlocal i
        i += 1
        return [i, "Something"]

    def closure(callback):
        return callback

    return closure(my_func)

func = parent_function()

def stars_decorator(input_function):
    def main_function(name):
        print(f"{"*" * (len(name) + 12)}\n* ", end="")
        input_function(name)
        print(f" *\n{"*" * (len(name) + 12)}")

    return main_function

@stars_decorator
def greet_someone(name):
    print(f"Hello, {name}!", end="")

#=========================#

if __name__ == "__main__":
    # for _ in range(10):
    #     print(func())
    greet_someone("Tom")