def fib(n):
    a=[0,1]
    for i in range(2,n+1):
        a.append(a[i-1]+a[i-2])
    return a[n]
#print fib(12)
def func(no_of_digits):
    i=20
    while(1):
        if(len(str(fib(i)))>=no_of_digits):
            return i
            break
        else:
            i=i+1
print func(1000)
