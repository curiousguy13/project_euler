import math
def sumPrimes(N):
    '''function to print sum of primes less than N'''
    '''it tries to divide every number by the prime numbers already encountered, 
    if it's divisible by any of them it's composite and flag=0 
    else it's prime and flag=1'''
    '''thought by me :) '''
    primes=[2]
    n=3
    while(1):
        flag=1
        if(n>=N):
            break
        for i in primes:
            if(i>math.sqrt(n)):
                break
            if(n%i==0):
                flag=0
                break
        if (flag==1):
            primes.append(n)
        
        n+=2
    return sum(primes)
print sumPrimes(2000000)