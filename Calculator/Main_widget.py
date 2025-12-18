from PySide6 import QtWidgets, QtCore, QtGui
import math


class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        main_layout = QtWidgets.QVBoxLayout(self)
        self.keyboard_layout = QtWidgets.QGridLayout()
        self.calculatorBarLayout = QtWidgets.QHBoxLayout()
        self.tipLayout = QtWidgets.QHBoxLayout()
        self.resize(350, 400)
        self.problem = ""
        self.tips = QtWidgets.QTextEdit()
        self.tipLayout.addWidget(self.tips)
        self.keyboard_layout.setSpacing(2)
        main_layout.addLayout(self.tipLayout)

        # Создание основных списков
        other_keys = ["C", "+", "-", "/", "*", "Xⁿ", "=", "√", ",", "π", "(", ")", "⌫"]
        other_keys = [QtWidgets.QPushButton(i) for i in other_keys]
        buttons = [QtWidgets.QPushButton(f"{i}") for i in range(10)]
        self.not_operators = [f"{i}" for i in range(10)]
        self.not_operators.append("π")
        
        # Стайл-листы
        
        for i in range(len(buttons)):
            buttons[i].setStyleSheet("""QPushButton { 
                                    color: #fcfcfc;
                                    background-color: #5e5e5e;
                                    padding: 10px;
                                    border-radius: 15px; 
                                    }
                                    QPushButton:hover {
                                     background-color: #4d4d4d;
                                    }
                                """)
        for i in range(len(other_keys)):
            other_keys[i].setStyleSheet("""QPushButton { 
                                    color: #fcfcfc;
                                    background-color: #3b3b3b;
                                    padding: 10px;
                                    border-radius: 15px; 
                                    }
                                    QPushButton:hover {
                                     background-color: #303030;
                                    }
                                        """)
        self.tips.setStyleSheet("background-color: #636363; color: #ffffff")
        self.setStyleSheet("background-color: #7d7d7d")

        # Создание клавиатуры чисел
    
        for i in range(3):
            for j in range(3):
                self.keyboard_layout.addWidget(buttons[3*i + j + 1], i + 1, j)
        self.keyboard_layout.addWidget(buttons[0], 4, 1)
        
        # Создание строки калькулятора 
        self.textEdit = QtWidgets.QLabel("  ")
        self.textEdit.setStyleSheet("""background-color: #262626;
                                    color: #fdfdfd""")
        self.calculatorBarLayout.addWidget(self.textEdit)
        self.textEdit.setGeometry(200, 200, 100, 100)
        buttons[6].setFlat(False)
        main_layout.addLayout(self.calculatorBarLayout)
        main_layout.addLayout(self.keyboard_layout)

        # Создание клавиатуры остальных кнопок
        
        self.keyboard_layout.addWidget(other_keys[0], 0, 0)
        self.keyboard_layout.addWidget(other_keys[1], 0, 3)
        self.keyboard_layout.addWidget(other_keys[2], 1, 3)
        self.keyboard_layout.addWidget(other_keys[3], 3, 3)
        self.keyboard_layout.addWidget(other_keys[4], 2, 3)
        self.keyboard_layout.addWidget(other_keys[5], 5, 2)
        self.keyboard_layout.addWidget(other_keys[6], 4, 3, 2, 1)
        # self.keyboard_layout.addWidget(other_keys[7], 5, 3)
        self.keyboard_layout.addWidget(other_keys[8], 4, 0)
        self.keyboard_layout.addWidget(other_keys[9], 4, 2)
        self.keyboard_layout.addWidget(other_keys[10], 5, 0)
        self.keyboard_layout.addWidget(other_keys[11], 5, 1)
        self.keyboard_layout.addWidget(other_keys[12], 0, 1)


        # Реакция на нажатия
        
        buttons[0].clicked.connect(self.add0)
        buttons[1].clicked.connect(self.add1)
        buttons[2].clicked.connect(self.add2)
        buttons[3].clicked.connect(self.add3)
        buttons[4].clicked.connect(self.add4)
        buttons[5].clicked.connect(self.add5)
        buttons[6].clicked.connect(self.add6)
        buttons[7].clicked.connect(self.add7)
        buttons[8].clicked.connect(self.add8)
        buttons[9].clicked.connect(self.add9)
        other_keys[0].clicked.connect(self.clear)
        other_keys[1].clicked.connect(self.add)
        other_keys[2].clicked.connect(self.sub)
        other_keys[3].clicked.connect(self.div)
        other_keys[4].clicked.connect(self.mul)
        other_keys[5].clicked.connect(self.power)
        other_keys[6].clicked.connect(self.count)
        # TODO other_keys[7]
        other_keys[8].clicked.connect(self.point)
        other_keys[9].clicked.connect(self.pi) #PI
        other_keys[10].clicked.connect(self.lbracket) #(
        other_keys[11].clicked.connect(self.rbracket) #)
        other_keys[12].clicked.connect(self.back)

        
    # То, что делается при нажатии

    @QtCore.Slot()
    def add0(self):
        self.textEdit.setText(self.textEdit.text() + "0")
        self.problem+="0"
    
    @QtCore.Slot()
    def add1(self):
        self.textEdit.setText(self.textEdit.text() + "1")
        self.problem+="1"
    
    @QtCore.Slot()
    def add2(self):
        self.textEdit.setText(self.textEdit.text() + "2")
        self.problem+="2"
    
    @QtCore.Slot()
    def add3(self):
        self.textEdit.setText(self.textEdit.text() + "3")
        self.problem+="3"
    
    @QtCore.Slot()
    def add4(self):
        self.textEdit.setText(self.textEdit.text() + "4")
        self.problem+="4"
    
    @QtCore.Slot()
    def add5(self):
        self.textEdit.setText(self.textEdit.text() + "5")
        self.problem+="5"
    
    @QtCore.Slot()
    def add6(self):
        self.textEdit.setText(self.textEdit.text() + "6")
        self.problem+="6"
    
    @QtCore.Slot()
    def add7(self):
        self.textEdit.setText(self.textEdit.text() + "7")
        self.problem+="7"
    
    @QtCore.Slot()
    def add8(self):
        self.textEdit.setText(self.textEdit.text() + "8")
        self.problem+="8"
    
    @QtCore.Slot()
    def add9(self):
        self.textEdit.setText(self.textEdit.text() + "9")
        self.problem+="9"
    
    @QtCore.Slot()
    def clear(self):
        self.textEdit.setText(" ")
        self.problem = ""
    
    @QtCore.Slot()
    def add(self):
        self.textEdit.setText(self.textEdit.text() + " + ")
        self.problem+=" + "
    
    @QtCore.Slot()
    def count(self):
        try:
            self.textEdit.setText(str(eval(self.problem)))
            self.problem = str(eval(self.problem))
        except ZeroDivisionError:
            self.textEdit.setText("Zero Division Error")
            self.problem = "0"
        except SyntaxError:
            if self.problem == "":
                self.textEdit.setText("0")
                self.problem = "0"
            else:
                self.tips.setText("Incorrect number format")

    @QtCore.Slot()
    def back(self):
        if self.textEdit.text()[-1] != " " and self.textEdit.text()[-1] != "π" and self.textEdit.text()[-1] != "(":
            self.textEdit.setText(self.textEdit.text()[:-1])
            self.problem = self.problem[:-1]
        elif self.textEdit.text()[-1] == "π":
            if self.textEdit.text()[-2] == "*":
                self.problem = self.problem[:-(len(str(math.pi)) + 1)]
            else:
                self.problem = self.problem[:-(len(str(math.pi)) + 1)]
            self.textEdit.setText(self.textEdit.text()[:-1])
        elif self.textEdit.text()[-1] == "(":
            self.problem = self.problem[:-2]
            self.textEdit.setText(self.textEdit.text()[:-1])
        elif self.textEdit.text()[-1] == " " and len(self.textEdit.text()) > 3:
            if self.textEdit.text()[-2] != "^":
                self.problem = self.problem[:-3]
            else:
                self.problem = self.problem[:-4]
            self.textEdit.setText(self.textEdit.text()[:-3])
        else:
            pass
        print(self.problem)

    
    @QtCore.Slot()
    def sub(self):
        self.textEdit.setText(self.textEdit.text() + " - ")
        self.problem+=" - "

    @QtCore.Slot()
    def div(self):
        self.textEdit.setText(self.textEdit.text() + " / ")
        self.problem+=" / "

    @QtCore.Slot()
    def mul(self):
        self.textEdit.setText(self.textEdit.text() + " * ")
        self.problem+=" * "

    @QtCore.Slot()
    def power(self):
        self.textEdit.setText(self.textEdit.text() + " ^ ")
        self.problem+=" ** "
    
    @QtCore.Slot()
    def point(self):
        self.textEdit.setText(self.textEdit.text() + ",")
        self.problem+="."

    @QtCore.Slot()
    def lbracket(self):
        if self.textEdit.text()[-1] == " ":
            self.problem+=" ("
        else:
            self.problem+="*("
        self.textEdit.setText(self.textEdit.text() + "(")

    @QtCore.Slot()
    def rbracket(self):
        self.problem+=")"
        self.textEdit.setText(self.textEdit.text() + ")")
    
    @QtCore.Slot()
    def pi(self):
        if self.textEdit.text()[-1] == " ":
            self.problem+=f"{math.pi}"
        else:
            self.problem+=f"*{math.pi}"
        self.textEdit.setText(self.textEdit.text() + "π")
        print(self.problem)
    