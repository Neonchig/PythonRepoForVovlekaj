import Widgets
import sys
from PySide6.QtWidgets import QSizePolicy
from PySide6 import QtWidgets, QtCore, QtGui



if __name__ == "__main__":
    
    app = QtWidgets.QApplication()

    widget = Widgets.Main()
    widget.show()

    sys.exit(app.exec())