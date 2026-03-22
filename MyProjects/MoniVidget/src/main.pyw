import sys, threading, time, sys, os
from pathlib import Path

from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

CounterThread = None
AppThread = None

def start_app():
    global click_counter
    global engine
    
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    path = ( Path( os.path.abspath( __file__ ) ) / ".." ).resolve()
    
    qml_file = path / "main.qml"
    engine.load(qml_file)

    root_object = engine.rootObjects()[0]
    click_counter = root_object.findChildren(QObject, "click_count")[0]
    backend = Backend()

    root_context = engine.rootContext()
    root_context.setContextProperty("backend", backend)
    
    if not engine.rootObjects():
        sys.exit(-1)

    
    sys.exit(app.exec())


class Backend(QObject):
    @Slot()
    def app_exit(self):
        countFlag = False
        with open("config", "w+") as file:
            file.write(str(click_counter.property("clicks")))
        engine.deleteLater()
        exit()

if __name__ == "__main__":
    AppThread = threading.Thread(target=start_app, daemon=True)
    AppThread.start()
    time.sleep(1.0)
