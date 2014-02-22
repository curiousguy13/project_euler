import math
def no_of_divisors(n):
    divisors=0
    for i in range(1,int(math.sqrt(n+1))+1):
        if (n%i==0):
            divisors+=1
    return divisors*2
def triangle(n):
    tri=[1]
    for i in xrange(1,100000):
        x=tri[i-1]+i+1
        tri.append(x)
        if(no_of_divisors(x)>=n):
            return x       
#print triangle(500)

list=[3,4,2]
print list.insert(0,100)