##given non empty array of integers sorted in ascending order
##Return a new array with square of inputs and also in sorted order
# time complexity - o(n)|space complexity o(n)
def sortedSquaredArray(array):
	# set up sorted array 
	sorted_array = [None]*len(array)
	# use two pointer approach both converging for loop termination
	left=0
	right=len(array)-1
	k = len(array)-1
	while left <=right:
		if abs(array[left]) > abs(array[right]):
			sorted_array[k] = array[left]**2
			left+=1
		else:
			sorted_array[k] = array[right]**2
			right-=1
		k-=1
	return sorted_array
