list1=[]
list1_size=int(input("Enter the size of array :"))
for i in range (0,list1_size):
    list1.append(int(input()))

print(list1)
flag=True
Find_num=int(input('Enter the number you want to serch :'))
length=len(list1)-1
flag=True
def linear_sesrch(Find_num):
    for i in range(0,list1_size):
        if list1[i]==Find_num:
            print("Number found at index : ",i," when using Linear Search")
            flag=True
            break
        else:
            flag=False

    if flag==False:
        print("Number not found at any index"+" when using Linear Search" )

def Binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return Binary_search(arr, low, mid - 1, x)
        else:
            return Binary_search(arr, mid + 1, high, x)
        
    else:
        return -1
    

linear_sesrch(Find_num)
result=Binary_search(list1,0,length,Find_num)
if(result!=-1):
    print("Number found at index : ",result," when using Binary Search")
else:
    print("Number not found at any index"+" when using Binary Search" )