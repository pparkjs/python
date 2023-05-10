import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore
from random import random
from PyQt5.Qt import QPixmap, QIcon, QSize

form_class = uic.loadUiType('my_omok01.ui')[0]

class MyWindow(QMainWindow, form_class):
    
   
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.flag = True
        for i in range(9+1):
            for j in range(9+1):
                btn = QPushButton('', self)
                btn.setIcon(QIcon("0.png"))
                btn.setIconSize(QSize(40, 40))
                btn.setGeometry(j*40, i*40, 40, 40) # j -> x축 i -> y축
                btn.clicked.connect(self.myclick)
                
        
    def myclick(self):
        if self.flag:
            self.sender().setIcon(QIcon("1.png")) #sender를  html에서 this라 생각하면 됨
        else:
            self.sender().setIcon(QIcon("2.png"))
        
        self.flag = not self.flag
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()