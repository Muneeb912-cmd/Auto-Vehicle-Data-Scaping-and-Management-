arr=[]
arr_size=int(input("Enter the size of array : "))
for i in range(0,arr_size):
    arr.append(int(input()))

def Insertion_Algo(arr):
    for i in range(1, len(arr)):     
        key = arr[i]        
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

print("Your array before : ",arr)
print("Your aerray after applying insertion sor method : ",Insertion_Algo(arr))