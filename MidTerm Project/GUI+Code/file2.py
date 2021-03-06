# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
from pandas.core.arrays.categorical import contains
from file3 import *

class Ui_LogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(692, 524)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pics/—Pngtree—avatar icon profile icon member_5247852.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LogIn.setWindowIcon(icon)
        LogIn.setStyleSheet("background-color:rgb(85, 255, 255)")
        self.label = QtWidgets.QLabel(LogIn)
        self.label.setGeometry(QtCore.QRect(130, 30, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LogIn)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(LogIn)
        self.label_3.setGeometry(QtCore.QRect(150, 150, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(LogIn)
        self.label_4.setGeometry(QtCore.QRect(40, 130, 101, 81))
        self.label_4.setStyleSheet("border-image: url(Pics/—Pngtree—avatar icon profile icon member_5247852.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(LogIn)
        self.label_5.setGeometry(QtCore.QRect(130, 250, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(LogIn)
        self.label_6.setGeometry(QtCore.QRect(130, 320, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.email = QtWidgets.QPlainTextEdit(LogIn)
        self.email.setGeometry(QtCore.QRect(240, 240, 311, 31))
        self.email.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.email.setObjectName("email")
        self.password = QtWidgets.QPlainTextEdit(LogIn)
        self.password.setGeometry(QtCore.QRect(240, 310, 311, 31))
        self.password.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.password.setObjectName("password")
        self.Signin = QtWidgets.QPushButton(LogIn)
        self.Signin.setGeometry(QtCore.QRect(330, 400, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Signin.setFont(font)
        self.Signin.setStyleSheet("background-color:rgb(255, 255, 255)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pics/icons8-login-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Signin.setIcon(icon1)
        self.Signin.setIconSize(QtCore.QSize(30, 30))
        self.Signin.setObjectName("Signin")

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)
        self.Signin.clicked.connect(self.Login1)
        self.Signin.clicked.connect(LogIn.close)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "SignUp"))
        self.label.setText(_translate("LogIn", "Welcome to Auto Vehicle"))
        self.label_2.setText(_translate("LogIn", "(Data Scraper and Manager)"))
        self.label_3.setText(_translate("LogIn", "Verify Yourself:"))
        self.label_5.setText(_translate("LogIn", "Email"))
        self.label_6.setText(_translate("LogIn", "Password"))
        self.Signin.setText(_translate("LogIn", "Sign In"))
# import sigin_rc
    def Login1(self,LogIn):
        super().__init__()
        email=self.email.toPlainText()
        try:
            password=int(self.password.toPlainText())
        except:
            print('input invalid')
        import pandas as pd
        
        column_names = ["email", "password"]
        df = pd.read_csv("LoginData.csv", names=column_names)
        list1=df.email.to_list()
        list2=df.password.to_list()
        if email in list1:
            if password in list2:
                self.window= QtWidgets.QWidget()
                self.ui=Ui_MainMenu()
                self.ui.setupUi(self.window)
                self.window.show()
                
            else:
                self.email.clear()
                self.password.clear()
                return False
        else:
            self.email.clear()
            self.password.clear()
            return False

