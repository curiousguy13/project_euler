l=[1,1]
for i in range(2,10001):
    l.append(l[i-1]*i)
print l[10000]

def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
#print fact(1000)