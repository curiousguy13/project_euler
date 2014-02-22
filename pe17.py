def letterCount(x):
	'''could have done this by hand'''
	letterSumOnes={0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
	letterSumTens={0:0,1:4,2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
	teens={10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
	k=(str(x))
	if(len(k)==1):
		return letterSumOnes[x]
	
	elif(len(k)==2):
		if(x in teens):
			return teens[x]
		else:
			return (letterSumTens[int(k[0])]+letterSumOnes[int(k[1])])
	elif(len(k)==3):
		if(int(k[1:]) in teens):
			return (letterSumOnes[int(k[0])]+10+teens[int(k[1:])])
		if (int(k[2])==0 and int(k[1])==0):
			return (letterSumOnes[int(k[0])]+7)
		else:
			return (letterSumOnes[int(k[0])]+letterSumTens[int(k[1])]+letterSumOnes[int(k[2])]+10)
sum=0
for i in range(1,1000):
	print i,':',letterCount(i)
	sum+=letterCount(i)
print sum
		
