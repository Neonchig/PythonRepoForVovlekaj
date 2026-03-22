import mouse, keyboard, time

def listen():
    if keyboard.is_pressed('alt'):
        mouse.click('right')
        time.sleep(0.25)
        print("smthng")

def main():
    while True:
        listen()
        time.sleep(0.01)

main()