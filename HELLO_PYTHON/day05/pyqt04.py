import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('pyqt04.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        num1 = int(self.le1.text())
        num2 = int(self.le2.text())
        sum = 0;
        
        for i in range(num1, num2+1):
            sum += i
            
        self.le3.setText(str(sum))
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()