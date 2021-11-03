#Bubble Sort for int and string data type
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


#Insertion Sort and string data type
def Insertion_Algo(arr):
    for i in range(1, len(arr)):     
        key = arr[i]        
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

#Merge Sort and string data types
def merge_sort(arr):
    if len(arr)>1:
        mid_point=(len(arr))//2
        L=arr[:mid_point]
        R=arr[mid_point:]
        merge_sort(L)
        merge_sort(R)

        i=0
        j=0
        k=0
        while i <len(L)and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1

    return arr 

#Quick Sort for int and string data types
def partition(nums, low, high):
      
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums): 
    def _quick_sort(items, low, high):
        if low < high:
            
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

#Selection Sort for int and string data types
def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j     
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

#Tim Sort for int and string data types
MINIMUM= 32
  
def find_minrun(n): 
  
    r = 0
    while n >= MINIMUM: 
        r |= n & 1
        n >>= 1
    return n + r 
  
def insertion_sort(array, left, right): 
    for i in range(left+1,right+1):
        element = array[i]
        j = i-1
        while element<array[j] and j>=left :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = element
    return array
              
def merge(array, l, m, r): 
  
    array_length1= m - l + 1
    array_length2 = r - m 
    left = []
    right = []
    for i in range(0, array_length1): 
        left.append(array[l + i]) 
    for i in range(0, array_length2): 
        right.append(array[m + 1 + i]) 
  
    i=0
    j=0
    k=l
   
    while j < array_length2 and  i < array_length1: 
        if left[i] <= right[j]: 
            array[k] = left[i] 
            i += 1
  
        else: 
            array[k] = right[j] 
            j += 1
  
        k += 1
  
    while i < array_length1: 
        array[k] = left[i] 
        k += 1
        i += 1
  
    while j < array_length2: 
        array[k] = right[j] 
        k += 1
        j += 1
  
def tim_sort(array): 
    n = len(array) 
    minrun = find_minrun(n) 
  
    for start in range(0, n, minrun): 
        end = min(start + minrun - 1, n - 1) 
        insertion_sort(array, start, end) 
   
    size = minrun 
    while size < n: 
  
        for left in range(0, n, 2 * size): 
  
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
            merge(array, left, mid, right) 
  
        size = 2 * size 

    print(array)
  
#Heap Sort for int and string data types
def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1    
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
  
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   
        heapify(arr, i, 0)






# ********************************************************************************************************************************
                                                                                                                                 
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem                                   
def SortCol(self,List,Method):    
    numcols =1         
    numrows=len(List)
    self.tableWidget.setColumnCount(numcols)
    self.tableWidget.setRowCount(numrows)   
                                                                                      
    # if List!="" and Method!="" :                                                                                                 
    if Method=="Bubble Sort":                                                                                                
            bubbleSort(List)                                                                                            
            # print(DispList)                                                                                                      
            for row in range(numrows):
                for column in range(numcols):                                                                                       
                    self.tableWidget.setItem(row, column, QTableWidgetItem((List[row])))
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()                                                 
                                                                                                                                 
    elif Method=="Merge Sort":                                                                                               
            DispList=merge_sort(List)                                                                                            
            # print(DispList)                                                                                                      
            for row in range(numrows):
                for column in range(numcols):                                                                                       
                    self.tableWidget.setItem(row, column, QTableWidgetItem((List[row])))
                                                                     
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()                                                                                                                     
                                                                                                                                 
    elif Method=="Heap Sort":                                                                                                
            DispList=heapSort(List)                                                                                              
            # print(DispList)                                                                                                      
            for row in range(numrows):
                for column in range(numcols):                                                                                       
                    self.tableWidget.setItem(row, column, QTableWidgetItem((List[row]))) 
                                                                    
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()                                                                                                                     
                                                                                                                                                                  
    elif Method=="Tim Sort":                                                                                                 
            DispList=tim_sort(List)                                                                                              
            # print(DispList)                                                                                                      
            for row in range(numrows):
                for column in range(numcols):                                                                                       
                    self.tableWidget.setItem(row, column, QTableWidgetItem((List[row])))                                                 
             
                                                                                                                                 
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
                                                                                                                                 
    elif Method=="Quick Sort":                                                                                               
            DispList=quick_sort(List)                                                                                            
            # print(DispList)                                                                                                      
            for row in range(numrows):
                for column in range(numcols):                                                                                       
                    self.tableWidget.setItem(row, column, QTableWidgetItem((List[row])))                                                 
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()                                                                                                                     
                                                                                                                                 
    elif Method=="Insertion Sort":                                                                                           
            DispList=Insertion_Algo(List)                                                                                        
            # print(DispList)                                                                                                      
            for row in range(numrows):
                for column in range(numcols):                                                                                       
                    self.tableWidget.setItem(row, column, QTableWidgetItem((List[row])))                                                 
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()                                                                                                                     
                                                                                                                                 
    elif Method=="Slection Sort":                                                                                            
            DispList=selectionSort(List)                                                                                         
            # print(DispList)                                                                                                      
            for row in range(numrows):
                for column in range(numcols):                                                                                       
                    self.tableWidget.setItem(row, column, QTableWidgetItem((List[row])))                                                 
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()                                                                                                                     
                                                                                                                                 
# ********************************************************************************************************************************



  







