# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sixth.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import file3 as f3
import SortingAlgos as Sort

class Ui_sorting(object):
    def setupUi(self, sorting):
        sorting.setObjectName("sorting")
        sorting.resize(788, 749)
        sorting.setStyleSheet("background-color:rgb(85, 255, 255)\n"
"")
        self.label_2 = QtWidgets.QLabel(sorting)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(sorting)
        self.label.setGeometry(QtCore.QRect(30, 30, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(sorting)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(sorting)
        self.frame.setGeometry(QtCore.QRect(70, 160, 651, 181))
        self.frame.setStyleSheet("background-color:rgb(255, 249, 175);\n"
"border :3px black; ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.method1 = QtWidgets.QComboBox(self.frame)
        self.method1.setGeometry(QtCore.QRect(200, 100, 321, 31))
        self.method1.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.method1.setObjectName("method1")
        self.method1.addItem("")
        self.method1.addItem("")
        self.method1.addItem("")
        self.method1.addItem("")
        self.method1.addItem("")
        self.method1.addItem("")
        self.method1.addItem("")
        self.method1.addItem("")
        self.method1.setItemText(7, "")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 60, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(80, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.colname1 = QtWidgets.QLineEdit(self.frame)
        self.colname1.setGeometry(QtCore.QRect(160, 60, 121, 21))
        self.colname1.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.colname1.setObjectName("colname1")
        self.apply1 = QtWidgets.QPushButton(self.frame)
        self.apply1.setGeometry(QtCore.QRect(300, 140, 75, 31))
        self.apply1.setStyleSheet("background-color:rgb(193, 255, 251)")
        self.apply1.setObjectName("apply1")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(66, 10, 531, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(300, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.colname1_2 = QtWidgets.QLineEdit(self.frame)
        self.colname1_2.setGeometry(QtCore.QRect(430, 60, 121, 21))
        self.colname1_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.colname1_2.setObjectName("colname1_2")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(560, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gobacksorting = QtWidgets.QPushButton(sorting)
        self.gobacksorting.setGeometry(QtCore.QRect(640, 680, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gobacksorting.setFont(font)
        self.gobacksorting.setStyleSheet("background-color:rgb(233, 255, 254)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pics/images (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gobacksorting.setIcon(icon)
        self.gobacksorting.setIconSize(QtCore.QSize(20, 20))
        self.gobacksorting.setObjectName("gobacksorting")
        self.pushButton = QtWidgets.QPushButton(sorting)
        self.pushButton.setGeometry(QtCore.QRect(620, 510, 91, 41))
        self.pushButton.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(sorting)
        self.label_7.setGeometry(QtCore.QRect(30, 350, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(sorting)
        self.tableWidget.setGeometry(QtCore.QRect(130, 400, 471, 261))
        self.tableWidget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.apply1.clicked.connect(self.Sort_columns)





        self.retranslateUi(sorting)
        QtCore.QMetaObject.connectSlotsByName(sorting)

    def retranslateUi(self, sorting):
        _translate = QtCore.QCoreApplication.translate
        sorting.setWindowTitle(_translate("sorting", "DataSorting"))
        self.label_2.setText(_translate("sorting", "(Data Scraper and Manager)"))
        self.label.setText(_translate("sorting", "Auto Vehicle"))
        self.label_3.setText(_translate("sorting", "Data Sorting :"))
        self.method1.setItemText(0, _translate("sorting", "Merge Sort"))
        self.method1.setItemText(1, _translate("sorting", "Heap Sort"))
        self.method1.setItemText(2, _translate("sorting", "Tim Sort"))
        self.method1.setItemText(3, _translate("sorting", "Quick Sort"))
        self.method1.setItemText(4, _translate("sorting", "Bubble Sort"))
        self.method1.setItemText(5, _translate("sorting", "Insertion Sort"))
        self.method1.setItemText(6, _translate("sorting", "Slection Sort"))
        self.label_4.setText(_translate("sorting", "Column Name"))
        self.label_5.setText(_translate("sorting", "Method"))
        self.apply1.setText(_translate("sorting", "Apply"))
        self.label_6.setText(_translate("sorting", "You can chose the name the column you want to sort from the Display window "))
        self.label_8.setText(_translate("sorting", "Number of Rows"))
        self.label_9.setText(_translate("sorting", "/10,48,576"))
        self.gobacksorting.setText(_translate("sorting", "Go Back"))
        self.pushButton.setText(_translate("sorting", "Clear Table"))
        self.label_7.setText(_translate("sorting", "Results of Sorting"))


    def Sort_columns(self):
            import pandas as pd
            try:
                df=pd.read_csv('Data.csv')
            except:
                print('Error in file Opening')

            col_name=self.colname1.text()
            NumRows=int(self.colname1_2.text())
            count=1
            List=[]
            if col_name.isalnum():
                try:
                    for items in (df[col_name]):
                        while count<=NumRows:
                            List.append(items)
                            count+=1
                except:
                    print("Wrong Column name")

                Method=self.method1.currentText()
                Sort.SortCol(self,List,Method)


            else:
                self.colname1.clear()







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sorting = QtWidgets.QWidget()
    ui = Ui_sorting()
    ui.setupUi(sorting)
    sorting.show()
    sys.exit(app.exec_())
