from PyQt6.QtWidgets import QMainWindow,QApplication, QMessageBox
from rimtointeger import *
import sys

"""
This program converts Rim numbers to Decimal Arabic numbers
"""
class RimToInt:
    def __init__(self, son:str):
        self.son = son
    dict1 = {
        "I" : 1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    def convert(self):
        try:
            temp = self.dict1[self.son[0]]
            summa = 0
            for i in self.son:
                if self.dict1[i] <= temp:
                    summa += self.dict1[i]
                    temp = self.dict1[i]
                else:
                    summa +=self.dict1[i]
                    summa -= temp * 2
                    temp = self.dict1[i]
        except Exception as ex:
            return "!!!!!!"
        else:
            return str(summa)



class Window(QMainWindow):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineinput.textChanged.connect((self.converter))

    def converter(self):
        text = self.ui.lineinput.text()
        if text != "":
            toRim = RimToInt(text)
            self.ui.labeloutput.setText(toRim.convert())

def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()