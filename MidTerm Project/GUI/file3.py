# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Third.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import file4 as f4
import file6 as f6
import file5 as f5


class Ui_MainMenu(object):
    def open_DataScrappingWindow(self):
        self.window= QtWidgets.QWidget()
        self.ui=f4.Ui_datadisplay()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def open_DataSortingWindow(self):
        self.window= QtWidgets.QWidget()
        self.ui=f6.Ui_sorting()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_DataSearchingWindow(self):
        self.window= QtWidgets.QWidget()
        self.ui=f5.Ui_SearchData()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(668, 585)
        font = QtGui.QFont()
        font.setUnderline(True)
        MainMenu.setFont(font)
        MainMenu.setStyleSheet("background-color:rgb(85, 255, 255)\n"
"")
        self.label = QtWidgets.QLabel(MainMenu)
        self.label.setGeometry(QtCore.QRect(30, 30, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainMenu)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainMenu)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.exitmain = QtWidgets.QPushButton(MainMenu)
        self.exitmain.setGeometry(QtCore.QRect(530, 490, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.exitmain.setFont(font)
        self.exitmain.setStyleSheet("background-color:rgb(193, 255, 251)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pics/icons8-exit-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitmain.setIcon(icon)
        self.exitmain.setIconSize(QtCore.QSize(50, 50))
        self.exitmain.setObjectName("exitmain")
        self.exitmain.clicked.connect(sys.exit)
        self.frame = QtWidgets.QFrame(MainMenu)
        self.frame.setGeometry(QtCore.QRect(60, 190, 531, 271))
        self.frame.setStyleSheet("background-color:rgb(255, 249, 175);\n"
"border :3px black; ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.scrapdata = QtWidgets.QPushButton(self.frame)
        self.scrapdata.setGeometry(QtCore.QRect(130, 40, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(11)
        self.scrapdata.setFont(font)
        self.scrapdata.setStyleSheet("background-color:rgb(212, 255, 249)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pics/download (3).jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scrapdata.setIcon(icon1)
        self.scrapdata.setIconSize(QtCore.QSize(50, 50))
        self.scrapdata.setObjectName("Display")
        self.scrapdata.clicked.connect(self.open_DataScrappingWindow)
        
        self.scrapdata.clicked.connect(MainMenu.close)
        self.searchdata = QtWidgets.QPushButton(self.frame)
        self.searchdata.setGeometry(QtCore.QRect(130, 180, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(11)
        self.searchdata.setFont(font)
        self.searchdata.setStyleSheet("background-color:rgb(212, 255, 249)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pics/download.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchdata.setIcon(icon2)
        self.searchdata.setIconSize(QtCore.QSize(50, 45))
        self.searchdata.setObjectName("searchdata")
        self.searchdata.clicked.connect(self.open_DataSearchingWindow)
        self.searchdata.clicked.connect(MainMenu.close)
        self.sortdata = QtWidgets.QPushButton(self.frame)
        self.sortdata.setGeometry(QtCore.QRect(130, 110, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(11)
        self.sortdata.setFont(font)
        self.sortdata.setStyleSheet("background-color:rgb(212, 255, 249)")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pics/images.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sortdata.setIcon(icon3)
        self.sortdata.setIconSize(QtCore.QSize(50, 50))
        self.sortdata.setObjectName("sortdata")
        self.sortdata.clicked.connect(self.open_DataSortingWindow)
        self.sortdata.clicked.connect(MainMenu.close)
        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Main"))
        self.label.setText(_translate("MainMenu", "Auto Vehicle"))
        self.label_2.setText(_translate("MainMenu", "(Data Scraper and Manager)"))
        self.label_3.setText(_translate("MainMenu", "Chose from the followng available options"))
        self.exitmain.setText(_translate("MainMenu", "Exit"))
        self.scrapdata.setText(_translate("MainMenu", "Load and Display Data from File"))
        self.searchdata.setText(_translate("MainMenu", "Data Searching                          "))
        self.sortdata.setText(_translate("MainMenu", "Data Sorting                                   "))

    

