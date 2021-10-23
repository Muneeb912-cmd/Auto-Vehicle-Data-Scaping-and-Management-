# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'foruth.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_datadisplay(object):
    def setupUi(self, datadisplay):
        datadisplay.setObjectName("datadisplay")
        datadisplay.resize(788, 666)
        datadisplay.setStyleSheet("background-color:rgb(170, 170, 255)\n"
"")
        self.label = QtWidgets.QLabel(datadisplay)
        self.label.setGeometry(QtCore.QRect(290, 30, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(datadisplay)
        self.label_2.setGeometry(QtCore.QRect(250, 70, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(datadisplay)
        self.progressBar.setGeometry(QtCore.QRect(130, 190, 531, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(datadisplay)
        self.label_3.setGeometry(QtCore.QRect(130, 160, 81, 16))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(datadisplay)
        self.tableWidget.setGeometry(QtCore.QRect(40, 250, 711, 331))
        self.tableWidget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gobackdatadisplay = QtWidgets.QPushButton(datadisplay)
        self.gobackdatadisplay.setGeometry(QtCore.QRect(660, 600, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gobackdatadisplay.setFont(font)
        self.gobackdatadisplay.setStyleSheet("background-color:rgb(233, 255, 254)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pics/images (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gobackdatadisplay.setIcon(icon)
        self.gobackdatadisplay.setIconSize(QtCore.QSize(20, 20))
        self.gobackdatadisplay.setObjectName("gobackdatadisplay")

        self.retranslateUi(datadisplay)
        QtCore.QMetaObject.connectSlotsByName(datadisplay)

    def retranslateUi(self, datadisplay):
        _translate = QtCore.QCoreApplication.translate
        datadisplay.setWindowTitle(_translate("datadisplay", "DataDisplay"))
        self.label.setText(_translate("datadisplay", "Auto Vehicle"))
        self.label_2.setText(_translate("datadisplay", "(Data Scraper and Manager)"))
        self.label_3.setText(_translate("datadisplay", "Scraping data "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("datadisplay", "Car Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("datadisplay", "Transmission"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("datadisplay", "Milage"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("datadisplay", "Car Model"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("datadisplay", "Engine"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("datadisplay", "Body Type"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("datadisplay", "Color"))
        self.gobackdatadisplay.setText(_translate("datadisplay", "Go Back"))
# import a10_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    datadisplay = QtWidgets.QWidget()
    ui = Ui_datadisplay()
    ui.setupUi(datadisplay)
    datadisplay.show()
    sys.exit(app.exec_())
