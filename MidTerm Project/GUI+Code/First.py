# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Firstpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import file1 as f1


class Ui_Form(object):
    def open_LogInWindow(self):
        self.window= QtWidgets.QWidget()
        self.ui=f1.Ui_Firstpage()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        n=500
        Form.setObjectName("Form")
        Form.resize(889, 608)
        Form.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 891, 611))
        self.widget.setStyleSheet("border-image: url(Pics/Capture.PNG);")
        self.widget.setObjectName("widget")
        self.progressBar1 = QtWidgets.QProgressBar(self.widget)
        self.progressBar1.setGeometry(QtCore.QRect(70, 470, 751, 23))
        self.progressBar1.setStyleSheet("border-image: url(Pics/download (1).png);")
        self.progressBar1.setObjectName("progressBar1")
        self.progressBar1.setMinimum(0)
        self.progressBar1.setMaximum(n)
        self.progressBar1.hide()==True
        self.label1 = QtWidgets.QLabel(self.widget)
        self.label1.setGeometry(QtCore.QRect(390, 510, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setStyleSheet("border-image: url(Pics/download (2).jpg);\n"
"color:white")
        self.label1.setObjectName("label1")
        self.label1.hide()==True
        self.Launch = QtWidgets.QPushButton(self.widget)
        self.Launch.setGeometry(QtCore.QRect(380, 280, 131, 51))
        self.Launch.setStyleSheet("border-image: url(Pics/launch.jpg);")
        self.Launch.setText("")
        self.Launch.setObjectName("Launch")
        self.Launch.clicked.connect(self.show_Bar_label)
        self.Launch.clicked.connect(lambda status,n_size=n:self.run(n_size))        
        self.Launch.clicked.connect(self.open_LogInWindow)
        self.Launch.clicked.connect(Form.close)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Welcome!!"))
        self.label1.setText(_translate("Form", "Loading Data!!"))
    
    def run(self,n):
        
        for i in range(n):
            time.sleep(0.01)
            self.progressBar1.setValue(i+1)


    def show_Bar_label(self):
        self.Launch.hide()==True
        self.label1.show()==True
        self.progressBar1.show()==True
        



