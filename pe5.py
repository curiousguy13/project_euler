'''brute-force-too slow'''
def small():
    n=1
    
    while(1):
        flag=1
        for i in range(1,12):
            if(n%i==0):
                continue
            else:
                flag=0
                break
        if(flag==1):
            return n
        n+=1

#print small()  
'''using recursion but it's even slower than brute force one'''
def small2(x):
    n=0
    if(x==1):
        return 1
    while(1):
        n+=1
        if(n%small2(x-1)==0):
            if(n%x==0):
                return n;
            else:
                continue
        else:
            continue
#print small2(7)
'''using dynamic programming--much faster :)'''
def small3(x):
    small=[0,1]
    n=1
    for i in range(2,x+1):
        n=small[i-1]
        while(1):
            if(n%i==0):
                small.append(n)
                break
            n+=small[i-1]
    return small
    
print small3(21)
                