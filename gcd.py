#program to find the gcd of two number
#using naive method
def gcd(a,b):
    la = []
    for i in range(1,a+1):
        if(a%i)==0:
            la.append(i)
    print(la)
    lb = []
    for j in range(1,b+1):
        if(b%j)==0:
            lb.append(j)
    print(lb)

    rl = []
    for r in la:
        for r in lb:
            if r in la and r in lb:
                rl.append(r)
    #print(rl)
    return (rl[-1])

#Driver code
a=int(input("enter first number"))
b=int(input("enter second number"))
print("gcd is :",gcd(a,b))