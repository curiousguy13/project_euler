
def collatz(x):
    '''brute force method '''
    l=[]
    while x!=1:
        l.append(x)
        if x%2==0:
            x=x/2
        else:
            x=3*x+1
    l.append(x)
    return l
#print collatz(7)
l={1:1}
def collatz2(x):
    '''dp method'''
    count=0
    
    if x in l :
        return count+int(l[x])
    else:
        if x%2==0:
            ans=x/2
        else:
            ans=3*x+1
        l[x]=collatz2(ans)+1
        return int(l[x])

print collatz2(1)


maxLen=0
maxPoint=0
for i in range(3,999999,2):
    n=(collatz2(i))
    if n>maxLen:
        maxLen=n
        maxPoint=i
print maxPoint



    
    
    

        

