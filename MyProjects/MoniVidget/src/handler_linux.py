from PySide6.QtCore import QObject
from PySide6.QtQml import QQmlApplicationEngine

import evdev

def handle_mouse(engine: QQmlApplicationEngine):
    devs = [evdev.InputDevice(path) for path in evdev.list_devices()]

    mouse = devs[0]

    root_object = engine.rootObjects()[0]

    click_counter = root_object.findChildren(QObject, "click_count")[0]

    with open("config", "r+") as file:
        click_counter.setProperty("clicks", int(file.readline()))

    for i in devs:
        if 1 in i.capabilities():
            if 272 in i.capabilities()[1] and 273 in i.capabilities()[1] and "ydotool" not in i.name and "Keyboard" not in i.name:
                mouse = i

    for event in mouse.read_loop():
        if event.type == 1 and event.code == 272 and event.value == 1:
            click_counter.setProperty("clicks", click_counter.property("clicks") + 1)