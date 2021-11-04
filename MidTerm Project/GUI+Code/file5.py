# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fifth.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import file3 as f3
import Searching_Methods as SM


class Ui_SearchData(object):
    def setupUi(self, SearchData):
        SearchData.setObjectName("SearchData")
        SearchData.resize(797, 767)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pics/download.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SearchData.setWindowIcon(icon)
        SearchData.setStyleSheet("background-color:rgb(85, 255, 255)\n"
"")
        self.gobacksearch = QtWidgets.QPushButton(SearchData)
        self.gobacksearch.setGeometry(QtCore.QRect(660, 700, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gobacksearch.setFont(font)
        self.gobacksearch.setStyleSheet("background-color:rgb(233, 255, 254)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pics/images (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gobacksearch.setIcon(icon1)
        self.gobacksearch.setIconSize(QtCore.QSize(20, 20))
        self.gobacksearch.setObjectName("gobacksearch")
        self.label_2 = QtWidgets.QLabel(SearchData)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(SearchData)
        self.progressBar.setGeometry(QtCore.QRect(150, 650, 531, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.tableWidget = QtWidgets.QTableWidget(SearchData)
        self.tableWidget.setGeometry(QtCore.QRect(40, 300, 711, 331))
        self.tableWidget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(7)
        # self.tableWidget.setRowCount(0)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(SearchData)
        self.label.setGeometry(QtCore.QRect(40, 20, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(SearchData)
        self.plainTextEdit.setGeometry(QtCore.QRect(570, 170, 191, 31))
        self.plainTextEdit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.search = QtWidgets.QPushButton(SearchData)
        self.search.setGeometry(QtCore.QRect(570, 250, 75, 23))
        self.search.setStyleSheet("background-color:rgb(233, 255, 254);\n"
"\n"
"")
        self.search.setIcon(icon)
        self.search.setObjectName("search")
        self.label_4 = QtWidgets.QLabel(SearchData)
        self.label_4.setGeometry(QtCore.QRect(520, 180, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(SearchData)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(SearchData)
        self.pushButton.setGeometry(QtCore.QRect(40, 220, 141, 41))
        self.pushButton.setStyleSheet("background-color:rgb(255, 255, 255)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Pics/images.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(SearchData)
        self.label_5.setGeometry(QtCore.QRect(580, 210, 61, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(SearchData)
        self.comboBox.setGeometry(QtCore.QRect(650, 210, 111, 31))
        self.comboBox.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.progressBar.hide()==True
        self.retranslateUi(SearchData)
        QtCore.QMetaObject.connectSlotsByName(SearchData)
         
        self.pushButton.clicked.connect(self.load_File)
        self.pushButton.clicked.connect(self.datahead)
        self.search.clicked.connect(self.Search)

    def retranslateUi(self, SearchData):
        _translate = QtCore.QCoreApplication.translate
        SearchData.setWindowTitle(_translate("SearchData", "SearchData"))
        self.gobacksearch.setText(_translate("SearchData", "Go Back"))
        self.label_2.setText(_translate("SearchData", "(Data Scraper and Manager)"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("SearchData", "Car Name"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("SearchData", "Milage"))
        # item = self.tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("SearchData", "Location"))
        # item = self.tableWidget.horizontalHeaderItem(3)
        # item.setText(_translate("SearchData", "Price"))
        # item = self.tableWidget.horizontalHeaderItem(4)
        # item.setText(_translate("SearchData", "Color"))
        # item = self.tableWidget.horizontalHeaderItem(5)
        # item.setText(_translate("SearchData", "Body Type"))
        # item = self.tableWidget.horizontalHeaderItem(6)
        # item.setText(_translate("SearchData", "Transmission"))
        self.label.setText(_translate("SearchData", "Auto Vehicle"))
        self.search.setText(_translate("SearchData", "Search"))
        self.label_4.setText(_translate("SearchData", "Search "))
        self.label_3.setText(_translate("SearchData", "Search Data"))
        self.pushButton.setText(_translate("SearchData", "Display Initial Data"))
        self.label_5.setText(_translate("SearchData", "Apply Filters"))
        self.comboBox.setItemText(0, _translate("SearchData", "Starts with"))
        self.comboBox.setItemText(1, _translate("SearchData", "Linear Search"))
        self.comboBox.setItemText(2, _translate("SearchData", "Ends With"))


    def load_File(self):
        import pandas as pd
        try:            
            self.all_data = pd.read_csv('Data.csv')
        except:
            print("An Error Occured!")

    def datahead(self):    
        NumRows = 50000
        self.tableWidget.setColumnCount(len(self.all_data.columns))
        self.tableWidget.setRowCount(NumRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)
        self.progressBar.show()==True
        count=1
        k=500    
        for i in range(NumRows):
            if i==k:
                self.progressBar.setValue(count)
                count+=1
                k=k+500
            for j in range(len(self.all_data.columns)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        if count==100:
            self.progressBar.hide()==True
            self.pushButton.setEnabled(True)

    def Search(self):
        self.tableWidget.clear
        Method=self.comboBox.currentText()
        text1=self.plainTextEdit.toPlainText()  
        SM.SearchData(self,text1,Method)



