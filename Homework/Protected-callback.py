def make_protected_callback(password, callback):
    user_input = input()
    check_password = lambda password, user_input, callback: callback() if password == user_input else "Access denied"
    return check_password(password, user_input, callback)

def say_hello():
    return "Hello"

print(make_protected_callback("xDP0rmpH/bi17rxwgntg", say_hello))