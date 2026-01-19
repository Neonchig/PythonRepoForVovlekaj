from evdev import InputDevice, UInput, ecodes
import threading, time

dev = InputDevice(str(input()))
dev.grab()  # Блокируем мышь

ui = UInput.from_device(dev, name='virtual-mouse')

running_left = False
running_right = False
blocked = True
thread = None

def loop_left():
    while running_left:
        ui.write(ecodes.EV_KEY, ecodes.BTN_LEFT, 1)
        ui.syn()
        time.sleep(0.025)
        ui.write(ecodes.EV_KEY, ecodes.BTN_LEFT, 0)
        ui.syn()
        time.sleep(0.025)

def loop_right():
    while running_right:
        ui.write(ecodes.EV_KEY, ecodes.BTN_RIGHT, 1)
        ui.syn()
        time.sleep(0.025)
        ui.write(ecodes.EV_KEY, ecodes.BTN_RIGHT, 0)
        ui.syn()
        time.sleep(0.025)

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY and event.code == ecodes.BTN_LEFT and not blocked:
        if event.value == 1: # Когда нажата
            if not running_left:
                running_left = True
                thread = threading.Thread(target=loop_left)
                thread.start()
            continue  # * Не пропускаем ЛКМ 
        elif event.value == 0: # Когда отпущена
            running_left = False
            continue  # * Все еще не пропускаем 
    
    if event.type == ecodes.EV_KEY and event.code == ecodes.BTN_RIGHT and not blocked:
        if event.value == 1: # Когда нажата
            if not running_right:
                running_right = True
                thread = threading.Thread(target=loop_right)
                thread.start()
            continue  # * Не пропускаем ЛКМ 
        elif event.value == 0: # Когда отпущена
            running_right = False
            continue  # * Все еще не пропускаем 

    if event.type == ecodes.EV_KEY and event.code == ecodes.BTN_MIDDLE:
        if event.value == 1:
            blocked = not(blocked)

    ui.write_event(event)
    ui.syn()