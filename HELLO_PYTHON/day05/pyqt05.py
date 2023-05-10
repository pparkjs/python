import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType('pyqt05.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        
        arr = []
        
        for i in range(1, 45+1):
            arr.append(i)
            
        for i in range(46):
            rnd = int(random()*45)
            a = arr[rnd]
            b = arr[0]
            arr[0] = a
            arr[rnd] = b
        
        self.t1.setText(str(arr[0]))
        self.t2.setText(str(arr[1]))
        self.t3.setText(str(arr[2]))
        self.t4.setText(str(arr[3]))
        self.t5.setText(str(arr[4]))
        self.t6.setText(str(arr[5]))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()