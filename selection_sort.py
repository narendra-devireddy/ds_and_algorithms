#selection sort|o(n^2) complexity|o(1) space
def selection_sort(array):
	#during each iteration find minimum element 
	# and swap based on the index
	# sort array builds progressively from left to right
	for i in range(len(array)):
		min_idx = -1
		min_value = float('inf')
		for j in range(i,len(array)):
			if array[j] < min_value:
				min_idx = j
				min_value = array[j]
		# check if min_idx is not changed 
		if min_idx >=0:
			array[i],array[min_idx]=array[min_idx],array[i]
	return array
