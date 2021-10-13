arr=[]
arr_size=int(input("Enter the size of array : "))
for i in range(0,arr_size):
    arr.append(int(input()))

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
       

print("the array you entered is : ",arr)      
print("The new array after merger sort is : ",merge_sort(arr))
