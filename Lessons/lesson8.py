global i

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

for _ in range(10):
    print(func())