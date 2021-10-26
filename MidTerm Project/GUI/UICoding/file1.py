# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from file2 import Ui_LogIn
import sys

class Ui_Firstpage(object):
        def open_LogInWindow(self):
              self.window= QtWidgets.QWidget()
              self.ui=Ui_LogIn()
              self.ui.setupUi(self.window)
              self.window.show()

        def setupUi(self, Firstpage):
                Firstpage.setObjectName("Firstpage")
                Firstpage.resize(764, 622)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Pics/images.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
                Firstpage.setWindowIcon(icon)
                Firstpage.setAutoFillBackground(False)
                Firstpage.setStyleSheet("background-color:rgb(85, 255, 255)\n"
                                        "")
                self.label = QtWidgets.QLabel(Firstpage)
                self.label.setGeometry(QtCore.QRect(140, 40, 451, 31))
                font = QtGui.QFont()
                font.setPointSize(26)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.label_3 = QtWidgets.QLabel(Firstpage)
                self.label_3.setGeometry(QtCore.QRect(170, 160, 321, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.label_2 = QtWidgets.QLabel(Firstpage)
                self.label_2.setGeometry(QtCore.QRect(190, 80, 391, 31))
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                self.signIn = QtWidgets.QPushButton(Firstpage)
                self.signIn.setGeometry(QtCore.QRect(490, 160, 91, 41))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.signIn.setFont(font)
                self.signIn.setStyleSheet("background-color:rgb(193, 255, 251)")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("Pics/icons8-login-30.png"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.signIn.setIcon(icon1)
                self.signIn.setIconSize(QtCore.QSize(50, 50))
                self.signIn.setObjectName("signIn")
                self.signIn.clicked.connect(self.open_LogInWindow)
                self.signIn.clicked.connect(Firstpage.close)
                self.frame = QtWidgets.QFrame(Firstpage)
                self.frame.setGeometry(QtCore.QRect(100, 220, 551, 251))
                self.frame.setStyleSheet("background-color:rgb(255, 249, 175);\n"
                                        "border :3px black; ")
                self.frame.setFrameShape(QtWidgets.QFrame.Panel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
                self.plainTextEdit.setGeometry(QtCore.QRect(190, 80, 271, 31))
                self.plainTextEdit.setStyleSheet(
                "background-color:rgb(255, 255, 255);\\nborder :3px black;")
                self.plainTextEdit.setObjectName("plainTextEdit")
                self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame)
                self.plainTextEdit_2.setGeometry(QtCore.QRect(190, 140, 271, 31))
                self.plainTextEdit_2.setStyleSheet(
                "background-color:rgb(255, 255, 255);\\nborder :3px black;")
                self.plainTextEdit_2.setObjectName("plainTextEdit_2")
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setGeometry(QtCore.QRect(50, 20, 111, 31))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.frame)
                self.label_5.setGeometry(QtCore.QRect(100, 90, 47, 13))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_5.setFont(font)
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.frame)
                self.label_6.setGeometry(QtCore.QRect(100, 140, 71, 16))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_6.setFont(font)
                self.label_6.setObjectName("label_6")
                self.signup = QtWidgets.QPushButton(self.frame)
                self.signup.setGeometry(QtCore.QRect(250, 190, 101, 31))
                self.signup.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("Pics/download (1).jpg"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.signup.setIcon(icon2)
                self.signup.setIconSize(QtCore.QSize(100, 100))
                self.signup.setObjectName("signup")
                self.pushButton_2 = QtWidgets.QPushButton(Firstpage)
                self.pushButton_2.setGeometry(QtCore.QRect(620, 520, 91, 41))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.pushButton_2.setFont(font)
                self.pushButton_2.setStyleSheet("background-color:rgb(193, 255, 251)")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("Pics/icons8-exit-30.png"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pushButton_2.setIcon(icon3)
                self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_2.clicked.connect(sys.exit)
                self.retranslateUi(Firstpage)
                QtCore.QMetaObject.connectSlotsByName(Firstpage)

        def retranslateUi(self, Firstpage):
                _translate = QtCore.QCoreApplication.translate
                Firstpage.setWindowTitle(_translate("Firstpage", "SDMS"))
                self.label.setText(_translate("Firstpage", "Welcome to Auto Vehicle"))
                self.label_3.setText(_translate(
                "Firstpage", "Already have an account? Click here"))
                self.label_2.setText(_translate(
                "Firstpage", "(Data Scraper and Manager)"))
                self.signIn.setText(_translate("Firstpage", "Sign In"))
                self.label_4.setText(_translate("Firstpage", "Sign Up"))
                self.label_5.setText(_translate("Firstpage", "Email"))
                self.label_6.setText(_translate("Firstpage", "Password"))
                self.pushButton_2.setText(_translate("Firstpage", "Exit"))

