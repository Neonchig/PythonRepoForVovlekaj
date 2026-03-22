from PySide6 import QtCore
import math

class functions():
    def __init__(self):
        self._problem = ""
        self._problem_mem = ""

    @property
    def problem(self) -> str:
        return self._problem
    
    @property
    def problem_mem(self) -> str:
        return self._problem_mem

    @problem.setter
    def problem(self, problem):
        self._problem = problem

    @problem_mem.setter
    def problem_mem(self, problem_mem):
        self._problem_mem = problem_mem


    def get_problem(self) -> str:
        return self._problem
    
    def set_problem(self, problem):
        self._problem = problem

    def get_problem_mem(self) -> str:
        return self._problem_mem
    
    def set_problem_mem(self, problem_mem):
        self._problem_mem = problem_mem
    
    def convert(value:str):

        value = str(value)
        value = str(value.replace("+", " + "))
        value = str(value.replace("-", " - "))
        value = str(value.replace("*", " * "))
        value = str(value.replace("/", " / "))
        value = str(value.replace(".", ","))
        value = str(value.replace(" * 3,1416 ", "π"))
        value = str(value.replace("3,1416", "π"))
        return value

    @QtCore.Slot()
    def A0(self) -> None:
        self.set_problem(self.get_problem() + "0")
        self.set_problem_mem(self.get_problem_mem() + "1")
    
    @QtCore.Slot()
    def A1(self) -> None:
        self.set_problem(self.get_problem() + "1")
        self.set_problem_mem(self.get_problem_mem() + "1")
    
    @QtCore.Slot()
    def A2(self) -> None:
        self.set_problem(self.get_problem() + "2")
        self.set_problem_mem(self.get_problem_mem() + "1")

    @QtCore.Slot()
    def A3(self) -> None:
        self.set_problem(self.get_problem() + "3")
        self.set_problem_mem(self.get_problem_mem() + "1")
    
    @QtCore.Slot()
    def A4(self) -> None:
        self.set_problem(self.get_problem() + "4")
        self.set_problem_mem(self.get_problem_mem() + "1")
    
    @QtCore.Slot()
    def A5(self) -> None:
        self.set_problem(self.get_problem() + "5")
        self.set_problem_mem(self.get_problem_mem() + "1")

    @QtCore.Slot()
    def A6(self) -> None:
        self.set_problem(self.get_problem() + "6")
        self.set_problem_mem(self.get_problem_mem() + "1")
    
    @QtCore.Slot()
    def A7(self) -> None:
        self.set_problem(self.get_problem() + "7")
        self.set_problem_mem(self.get_problem_mem() + "1")
    
    @QtCore.Slot()
    def A8(self) -> None:
        self.set_problem(self.get_problem() + "8")
        self.set_problem_mem(self.get_problem_mem() + "1")
    
    @QtCore.Slot()
    def A9(self) -> None:
        self.set_problem(self.get_problem() + "9")
        self.set_problem_mem(self.get_problem_mem() + "1")

    @QtCore.Slot()
    def AC(self) -> None:
        self.set_problem("")
        self.set_problem_mem("")
    
    @QtCore.Slot()
    def APl(self) -> None:
        self.set_problem(self.get_problem() + "+")
        self.set_problem_mem(self.get_problem_mem() + "1")
    
    @QtCore.Slot()
    def AMi(self) -> None:
        self.set_problem(self.get_problem() + "-")
        self.set_problem_mem(self.get_problem_mem() + "1")

    @QtCore.Slot()
    def AMu(self) -> None:
        self.set_problem(self.get_problem() + "*")
        self.set_problem_mem(self.get_problem_mem() + "1")

    @QtCore.Slot()
    def ADi(self) -> None:
        self.set_problem(self.get_problem() + "/")
        self.set_problem_mem(self.get_problem_mem() + "1")

    @QtCore.Slot()
    def AEq(self) -> None:
        self.set_problem(eval(self.get_problem()))

    @QtCore.Slot()
    def APw(self):
        self.set_problem(self.get_problem() + "**")
        self.set_problem_mem(self.get_problem_mem() + "2")
    
    @QtCore.Slot()
    def ASq(self):
        # self.set_problem(self.get_problem() + "") # TODO
        pass

    @QtCore.Slot()
    def APo(self) -> None:
        self.set_problem(self.get_problem() + ".")
        self.set_problem_mem(self.get_problem_mem() + "1")

    @QtCore.Slot()
    def APi(self) -> None:
        if self.problem[-1] in ["+", "-", "*", "/", "("]:
            self.set_problem(self.get_problem() + f"{round(math.pi, 4)}") # TODO: Сделать авто-добавление умножения перед пи
            self.set_problem_mem(self.get_problem_mem() + "6")
        else:
            self.set_problem(self.get_problem() + f"*{round(math.pi, 4)} ")
            self.set_problem_mem(self.get_problem_mem() + "8")


    @QtCore.Slot()
    def ABL(self) -> None:
        self.set_problem(self.get_problem() + "(")
        self.set_problem_mem(self.get_problem_mem() + "1")

    @QtCore.Slot()
    def ABR(self) -> None:
        self.set_problem(self.get_problem() + ")")
        self.set_problem_mem(self.get_problem_mem() + "1")

    @QtCore.Slot()
    def ABa(self) -> None:
        self.set_problem(self.get_problem()[:-(int(self.get_problem_mem()[-1]))])
        self.set_problem_mem(self.get_problem_mem()[:-1])
    
    @QtCore.Slot()
    def AG(self) -> None:
        print(self.get_problem())
        print(self.get_problem_mem())
