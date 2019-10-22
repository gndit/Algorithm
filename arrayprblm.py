def arry_game(a):
    reached=0
    last_indx=len(a)-1
    i=0
    while i<=reached and reached<last_indx:
        reached=max(reached,a[i]+i)
        i+=1
    return reached>=last_indx
b=[2,2,0,1,2,0,2]
print(arry_game(b))