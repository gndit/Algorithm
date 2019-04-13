
#searching element using binary search algorithm
def bsearch(arr,n,x):
    i=0
    mid=(i+l)//2
    for d in range(n):
        if (arr[mid] == x):
            return mid
        else:
            if (arr[mid] > x):
                mid = mid - 1
            else:
                mid = mid + 1
    return -1


#driver code
#arr=[]
#z=input("Enter element in sorted order in array")
#for z in range(arr):
 #   arr.append(z)
arr=[1,3,5,7,13,14,16,64,76]
#x=64
x=int(input("enter any number that you want to search"))
n=len(arr)
l=n-1
print(x,"is persent at index",bsearch(arr,n,x))





