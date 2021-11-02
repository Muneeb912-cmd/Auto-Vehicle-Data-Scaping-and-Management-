from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
import First as f1
import pandas as pd
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time


# **********************************************Main Method*******************************************************
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = f1.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

# **********************************************Main Method*******************************************************

# def loaddata(self):
#         people=[{"name":"John","age":45,"address":"New York"}, {"name":"Mark", "age":40,"address":"LA"},
#                 {"name":"George","age":30,"address":"London"}]
#         row=0
#         self.tableWidget.setRowCount(len(people))
#         for person in people:
#             self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person["name"]))
#             self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(person["age"])))
#             self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person["address"]))
#             row=row+1
























def load_File(self):
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
        self.LoadData.hide()==True
        self.progressBar.hide()==True
        self.label_4.show()==True
