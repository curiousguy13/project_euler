import math

def largestPrimeFactor(n):
    '''simple brute force method to find the prime factors of a number n and return the largest of them'''
    ans=n
    for i in range(2,int(math.ceil((n**0.5))+1)):
        if(n%i==0 and isPrime(i)):
            ans=i
    return ans

def isPrime(n):
    '''to check if a given number n is prime or not by checking ts divisibility in range of numbers 
       from 2 to sqrt(n).
       if it is divisible by any of the numbers return False else return True''' 
    for i in range(2,int(math.ceil((n**0.5))+1)):
        if(n%i==0):
            return False
    return True
#print largestPrimeFactor(21)
#print largestPrimeFactor(600851475143)
#print isPrime(486847)

def largestPrimeFactor2(n):
    '''http://math.stackexchange.com/questions/389675/largest-prime-factor-of-600851475143'''
    '''Example: Let's find the largest prime factor of 105 using the method described above.

    Let (1) = 105. (2) = 2 (we always start with 2), and we don't have a value for (3) yet.

    Is (1) divisible by (2)? No. Increment (2) by +1: (2) = 3. Is Is (1) divisible by (2)? Yes. (105/3 = 35). 
    The largest divisor found so far is 3. Let (3) = 3. Update (1) = 35. Reset (2) = 2.
    Now, is (1) divisible by (2)? No. Increment (2) by +1: (2) = 3. Is (1) divisible by (2)? No. Increment (2) by +1: (2) = 4.
    Is (1) divisible by (2)? No. Increment (2) by +1: (2) = 5. Is (1) divisible by (2)? Yes. (35/5 = 7).
    The largest divisor we found previously is stored in (3). (3) is currently 3. 5 is larger than 3, so we update (3) = 5. We update (1)=7.
    We reset (2)=2.
    Then we repeat the process for (1), but we will just keep incrementing (2) until (2)=(1), because 7 is prime and has no divisors other than itself and 1.
    (We could already stop when (2)>((1)/2), as you cannot have integer divisors greater than half of a number - the smallest possible divisor (other than 1) of any number is 2!)
    
    So at that point we return (1) = 7.'''
    
    ''' i used 2 variables ie n and i instead of 3'''

    while(1):
        i=2
        while(i<n+1):
            if(n%i==0):
                if(i==n):
                    return i
                n=n/i
                break
            i+=1
print largestPrimeFactor2(600851475143)
