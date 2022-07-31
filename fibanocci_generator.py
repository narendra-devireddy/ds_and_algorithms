#fibanocci series generator
# the list can be generated using list(fibanocci_generator(n))
def fibanocci_generator(n):
	a,b=0,1
	i=0
	while i <n:
		yield a
		a,b = b,a+b
		i+=1
