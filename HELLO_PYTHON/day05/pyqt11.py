import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType('pyqt11.ui')[0]

class MyWindow(QMainWindow, form_class):
    
   
    def __init__(self):
        super().__init__()
        self.com = ""
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.setRandomCom()
        
    def myclick(self):
        print(self.com)
        mine = self.le.text()
        txt = ""
        s = 0
        b = 0
        s1 = self.com[0:1] 
        s2 = self.com[1:2]
        s3 = self.com[2:3]
        
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        if s1 == m1:
            s += 1
        if s2 == m2:
            s += 1
        if s3 == m3:
            s += 1
        
        if m1 == s2 or m1 == s3:
            b += 1
        if m2 == s1 or m2 == s3: 
            b += 1
        if m3 == s1 or m3 == s2:
            b += 1
        
        str_new = "{} \t {}S {}B\n".format(mine,s,b)
        str_old = self.pte.toPlainText()
        
        self.pte.setPlainText(str(str_old) + str(str_new))
        self.le.setText("")
        
        if s == 3:
            QMessageBox.about(self,'result', "정답입니다.")
        
    def setRandomCom(self):
        arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        for i in range(100):
            rnd = int(random()*9)
            a = arr[rnd]
            b = arr[0]
            arr[0] = a
            arr[rnd] = b
        
        self.com = arr[0]+arr[1]+arr[2]
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()