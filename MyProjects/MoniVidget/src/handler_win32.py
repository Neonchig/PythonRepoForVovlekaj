from PySide6.QtCore import QObject
from PySide6.QtQml import QQmlApplicationEngine

from pynput import mouse

def handle_mouse(engine: QQmlApplicationEngine):
    
    root_object = engine.rootObjects()[0]

    click_counter = root_object.findChildren(QObject, "click_count")[0]

    def add_click(x:int, y:int, key, pressed):
        if key == mouse.Button.left and pressed == True:
            click_counter.setProperty("clicks", click_counter.property("clicks") + 1)

    mouse.Listener(on_click=add_click)