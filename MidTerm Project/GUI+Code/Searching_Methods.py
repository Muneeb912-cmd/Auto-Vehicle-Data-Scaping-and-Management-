from typing import List


def Linear_search(arr, x):
    list_index=[]
    for i in range(len(arr)):  
        if arr[i] == x:
            list_index.append(i)
  
    return list_index

def startswith(arr,x):
    list_index=[]
    for i in range(len(arr)):
        if arr[i].startswith(x):
            list_index.append(i)
    
    return list_index

def endswith(arr,x):
    list_index=[]
    for i in range(len(arr)):
        if arr[i].endswith(x):
            list_index.append(i)
    
    return list_index



def SearchData(self,text1,method):
    import pandas as pd
    
    from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem

    try:            
        all_data = pd.read_csv('Data.csv')
    except:
        print("An Error Occured!")
    list=[]
    for items in all_data:
        list.append(items)
    
    index_list=[]
   
    if method=='Starts with"':
        returnedlist=startswith(list, text1)
        for i in returnedlist:
            index_list.append(i)
    elif method=='Linear Search':
        returnedlist=Linear_search(list, text1)
        for i in Linear_search(list, text1):
            index_list.append(i)
    elif method=='Ends With':
        returnedlist=endswith(list, text1)
        for i in endswith(list, text1):
            index_list.append(i)

    numrows=len(index_list)
    numcols=1
    
    for row in range(numrows):
        for column in range(numcols):
            for i in index_list:                                                                                       
                self.tableWidget.setItem(row, column, QTableWidgetItem((list[i])))
    self.tableWidget.resizeColumnsToContents()
    self.tableWidget.resizeRowsToContents()
    
