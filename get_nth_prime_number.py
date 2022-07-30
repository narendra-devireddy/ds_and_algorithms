##Get nth prime number
def get_nth_prime_number(n):
	#start with 2, the first prime number
	num = 2
	count = 1
	if n==1:
		return num 
	#for higher numbers
	while True:
		num+=1
		prime_number = True
		for i in range(2,(num//2)+1):
			if num%i == 0:
				prime_number = False
				break
		if prime_number:
			count+=1
			if count == n:
				return num