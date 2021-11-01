# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'foruth.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
import file3 as f3
import pandas as pd


class Ui_datadisplay(object):
    def setupUi(self, datadisplay):
        self.thread = {}
        datadisplay.setObjectName("datadisplay")
        datadisplay.resize(985, 801)
        datadisplay.setStyleSheet("background-color:rgb(85, 255, 255)\n"
                                  "")
        self.label = QtWidgets.QLabel(datadisplay)
        self.label.setGeometry(QtCore.QRect(380, 20, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(datadisplay)
        self.label_2.setGeometry(QtCore.QRect(340, 60, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(datadisplay)
        self.progressBar.setGeometry(QtCore.QRect(190, 680, 651, 23))
        # self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(datadisplay)
        self.label_3.setGeometry(QtCore.QRect(190, 650, 81, 16))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(datadisplay)
        self.tableWidget.setGeometry(QtCore.QRect(40, 220, 901, 411))
        self.tableWidget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gobackdatadisplay = QtWidgets.QPushButton(datadisplay)
        self.gobackdatadisplay.setGeometry(QtCore.QRect(840, 720, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gobackdatadisplay.setFont(font)
        self.gobackdatadisplay.setStyleSheet(
            "background-color:rgb(233, 255, 254)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pics/images (1).png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gobackdatadisplay.setIcon(icon)
        self.gobackdatadisplay.setIconSize(QtCore.QSize(20, 20))
        self.gobackdatadisplay.setObjectName("gobackdatadisplay")

        self.LoadData = QtWidgets.QPushButton(datadisplay)
        self.LoadData.setGeometry(QtCore.QRect(400, 160, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LoadData.setFont(font)
        self.LoadData.setStyleSheet("background-color:rgb(255, 255, 255)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pics/download (3).jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LoadData.setIcon(icon1)
        self.LoadData.setIconSize(QtCore.QSize(45, 45))
        self.LoadData.setObjectName("LoadData")
        self.LoadData.clicked.connect(self.woker1)
        # self.LoadData.clicked.connect(self.dataHead)
        self.label_4 = QtWidgets.QLabel(datadisplay)
        self.label_4.setGeometry(QtCore.QRect(50, 170, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(datadisplay)
        self.label_5.setGeometry(QtCore.QRect(340, 140, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3.hide() == True
        self.label_4.hide() == True
        self.label_5.hide() == True
        self.progressBar.hide() == True
        self.gobackdatadisplay.clicked.connect(self.open_MainWindow1)
        self.retranslateUi(datadisplay)
        QtCore.QMetaObject.connectSlotsByName(datadisplay)

    def retranslateUi(self, datadisplay):
        _translate = QtCore.QCoreApplication.translate
        datadisplay.setWindowTitle(_translate("datadisplay", "DataDisplay"))
        self.label.setText(_translate("datadisplay", "Auto Vehicle"))
        self.label_2.setText(_translate(
            "datadisplay", "(Data Scraper and Manager)"))
        self.label_3.setText(_translate("datadisplay", "Loading..."))
        self.gobackdatadisplay.setText(_translate("datadisplay", "Go Back"))
        self.LoadData.setText(_translate("datadisplay", "Load and Display"))
        self.label_4.setText(_translate(
            "datadisplay", "Data From CSV file successfully Loaded and displayed"))
        self.label_5.setText(_translate(
            "datadisplay", "Please Wait Data Is Loading...."))

    def woker1(self):
        self.thread1=ThreadClass()
        self.label_3.show() == True
        self.label_5.show() == True
        self.LoadData.hide() == True
        self.progressBar.show() == True
        self.thread1.start()
   

    def Display_Label_ProgressBar(self):
        self.label_3.show() == True
        self.label_5.show() == True
        self.LoadData.hide() == True
        self.progressBar.show() == True

    def open_MainWindow1(self):
        self.window = QtWidgets.QWidget()
        self.ui = f3.Ui_MainMenu()
        self.ui.setupUi(self.window)
        self.window.show()    
        

class ThreadClass(QtCore.QThread):
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        
    
    def run(self):
        try:
            self.all_data = pd.read_csv('Data.csv')
        except:
            print("An Error Occured!")
        self.LoadData.setEnabled(False)
        NumRows = len(self.all_data.index)
        self.tableWidget.setColumnCount(len(self.all_data.columns))
        self.tableWidget.setRowCount(NumRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)
        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    datadisplay = QtWidgets.QWidget()
    ui = Ui_datadisplay()
    ui.setupUi(datadisplay)
    datadisplay.show()
    sys.exit(app.exec_())
