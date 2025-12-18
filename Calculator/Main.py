import Main_widget
import sys
from PySide6.QtWidgets import QSizePolicy
from PySide6 import QtWidgets, QtCore, QtGui



if __name__ == "__main__":
    
    app = QtWidgets.QApplication()

    widget = Main_widget.Main()
    widget.show()

    sys.exit(app.exec())