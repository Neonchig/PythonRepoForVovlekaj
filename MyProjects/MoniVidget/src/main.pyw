import sys, threading, time, sys
from pathlib import Path

from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine




AppThread = None

def start_app():
    global engine
    
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qml_file = Path("src/main.qml")
    
    engine.load(qml_file)
    
    backend = Backend()

    root_context = engine.rootContext()
    root_context.setContextProperty("backend", backend)
    
    if not engine.rootObjects():
        sys.exit(-1)
    
    sys.exit(app.exec())


class Backend(QObject):
    @Slot()
    def app_exit(self):
        engine.deleteLater()
        exit()

if __name__ == "__main__":
    AppThread = threading.Thread(target=start_app, daemon=True)
    AppThread.start()
    time.sleep(0.4)
    
    if sys.platform == "linux":
        import handler_linux as handler
        handler.handle_mouse(engine)
    elif sys.platform == "win32":
        import handler_win32 as handler
        handler.handle_mouse(engine)
