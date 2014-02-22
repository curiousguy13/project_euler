def d(x):
	import math
	sum=0
	for i in range(1,int(math.ceil(x**0.5))):
		if(x%i==0):
			sum+=i
			sum+=(x/i)
	return sum-x
import time
start=time.time()
amicable=[]
for i in range(2,10001):
	k=d(i)
	if d(k)==i and k!=i:
		amicable.append(i)
print sum(amicable)
elapsed=time.time()-start
print 'time taken:',elapsed

