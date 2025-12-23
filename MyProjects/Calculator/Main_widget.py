from PySide6 import QtWidgets, QtCore, QtGui
import Behaviour
    
class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(800, 600)
        
        self.functions = Behaviour.functions()

        main_layout = QtWidgets.QVBoxLayout(self)
        main_kb = self.add_main_kb()
        self.calc_layout = self.add_calc_layout()
        main_layout.addWidget(self.calc_layout)
        main_layout.addLayout(main_kb)


    def add_basic_kb(self):
        
        Keyboard_Layout = QtWidgets.QGridLayout()
        
        # Клавиатура с числами
        numeric_keys_technical = list(range(10))
        numeric_keys = [QtWidgets.QPushButton(f"{i}") for i in range(10)]

        for i in range(len(numeric_keys)):
            method = getattr(self.functions, f"A{numeric_keys_technical[i]}")
            numeric_keys[i].clicked.connect(method)
            numeric_keys[i].clicked.connect(self.move_problem_to_calc)
        
        for i in range(3):
            for j in range(3):
                Keyboard_Layout.addWidget(numeric_keys[3 * i + j + 1], i + 1, j)

        Keyboard_Layout.addWidget(numeric_keys[0], 4, 0)

        return Keyboard_Layout
    
    def add_main_kb(self):
        basic_kb = self.add_basic_kb()
        
        # Клавиатура с операторами, знаками, etc
        other_keys_technical = ["C", "Pl", "Mi", "Mu", "Di", "Eq", "Pw", "Sq", "Po", "Pi", "BL", "BR", "Ba", "G"] 
        other_keys = ["C", "+", "-", "*", "/", "=", "Xⁿ", "√", ",", "π", "(", ")", "⌫", "G"]        
        other_keys = [QtWidgets.QPushButton(f"{i}") for i in other_keys]

        for i in range(len(other_keys)):
            method = getattr(self.functions, f"A{other_keys_technical[i]}")
            other_keys[i].clicked.connect(method)
            other_keys[i].clicked.connect(self.move_problem_to_calc)

        basic_kb.addWidget(other_keys[0], 0, 0) # C
        basic_kb.addWidget(other_keys[1], 1, 3) # +
        basic_kb.addWidget(other_keys[2], 2, 3) # -
        basic_kb.addWidget(other_keys[3], 3, 3) # *
        basic_kb.addWidget(other_keys[4], 4, 3) # /
        basic_kb.addWidget(other_keys[5], 4, 2) # =
        basic_kb.addWidget(other_keys[6], 0, 2) # ^/**
        basic_kb.addWidget(other_keys[7], 0, 3) # ! sqrt
        basic_kb.addWidget(other_keys[8], 4, 1) # ,/.
        basic_kb.addWidget(other_keys[9], 5, 2) # Pi
        basic_kb.addWidget(other_keys[10], 5, 0) # (
        basic_kb.addWidget(other_keys[11], 5, 1) # )
        basic_kb.addWidget(other_keys[12], 0, 1) # back
        basic_kb.addWidget(other_keys[13], 5, 3) # Get problem

        return basic_kb
    
    def add_calc_layout(self):
        
        calc_layout = QtWidgets.QLabel()

        return calc_layout
    
    def move_to_calc(self, value):
        
        self.calc_layout.setText(value)

    def convert(self, value:str):

        value = value.replace("+", " + ")
        value = value.replace("-", " - ")
        value = value.replace("*", " * ")
        value = value.replace("/", " / ")
        value = value.replace(".", ",")
        value = value.replace(" * 3,1416 ", "π")
        value = value.replace("3,1416", "π")
        """
        TODO: перенести эту часть в Behaviour
        TODO: Доделать метод convert
        * I'm sooo tired T_T *
        """
        return value

    @QtCore.Slot()
    def move_problem_to_calc(self):
        converted_problem = self.convert(self.functions.get_problem())
        self.calc_layout.setText(converted_problem)