#check if total is possible or not by adding list element
a=[1,0,-2,6,57,3,7,9,76]
total=60
count=0
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[i]+a[j]==total:
            count=1
        else:
            pass

if count == 1:
    print("total is possible")
else:
    print("Not possible")






