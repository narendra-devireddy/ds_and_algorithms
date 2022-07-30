#sqrt of a number without using operator or lib functions
# interview question - Data Science 
def sqrt_number(n):
	low = 0
	high=n
	potential_ = (low+high)/2
	while abs(potential_*potential_ - n) > 0.001:
		if potential_*potential_ > n:
			high=(low+high)/2
		elif potential_*potential_ < n:
			low=(low+high)/2
		potential_ = (low+high)/2
		print(potential_)
	return round(potential_,3)