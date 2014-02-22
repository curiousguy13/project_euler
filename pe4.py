
def isPalindrome(n):
    s=str(n)
    for i in range(len(s)/2+1):
        if(s[i]!=s[-i-1]):
            return False
    return True
#print isPalindrome(0)

def findPal():
    max=0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            if(isPalindrome(i*j)):
                if(max<i*j):
                    max=i*j
    return max
print findPal()