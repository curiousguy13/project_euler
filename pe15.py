def route(x):
	s=1
	for i in range(0,x):
		s*=(2*x-i)
		s/=(i+1)
	return s
print route(20)
