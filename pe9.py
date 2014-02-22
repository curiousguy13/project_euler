
def pythagoras(n):
    for i in range(1,n):
        for j in range(1,n):
            for k in range(1,n):
                if(i+j+k==n):
                    if(i**2+j**2==k**2):
                        print i,j,k
                        return i*j*k
print pythagoras(1000)