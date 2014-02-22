def sumOfFactors(x):
	'''return the sum of all the factors of a number x'''
	import math
	sum=0
	for i in range(1,int(math.sqrt(x)+1)):
		if x%i==0:
			sum+=i+x/i
	return sum-x
def abundant(x):
	'''return a list of abundant numbers till x'''
	abundantNos=[]
	for i in range(1,x+1):
		if sumOfFactors(i)>i: 
			abundantNos.append(i)
	return abundantNos
a=abundant(8123)
'''def notSumAbundant(x):
	for i in a:
		for j in a:
			if (i+j)==x:
				return False
			if j>x:
				break
		if i>x:
			break
	return True'''
def sol1(x):
	l=[]
	b=a
	for i in a:
		for j in b:
			if (i+j<x):
				l.append(i+j)
		b.remove(i)
	return list(set(l))


l=[k for k in range(1,8124)]
li=sol1(8123)
print li
sum1=sum(li)
sum2= sum(l)
print sum2-sum1



			
