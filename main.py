#Лыков Илья Николаевич 9 вариант
import sys
from PyQt5 import QtWidgets
import y
from math import log

def calc(str):
    x = str.split(", ")
    result = list()
    for i in x:
        i = float(i)
        if i > -1:
            y = i + 2 * i * i
        elif i <= -1:
            y = log(abs(i + 2)) * i
        result.append(str(y))
    result = ", ".join(result)
    return result

class App(QtWidgets.QMainWindow, y.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        x = self.lineEdit.text()
        x = x.split(", ")
        result = []
        for i in x:
            i = float(i)
            if i > -1:
                y = i + 2 * i * i
            elif i <= -1:
                y = log(abs(i+2))*i
            result.append(str(y))
        result = ", ".join(result)
        self.lineEdit_2.setText(result)

def main():

    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()