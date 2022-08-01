#bubble sort|o(n^2) complexity|o(1) space
def bubble_sort(array):
	is_sorted = False
	count = 0
	## we enter the loop assuming that array is not sorted
	while not is_sorted:
		#upon entry, iterate until we found some elements out of place
		#else we assume that array is sorted
		is_sorted = True
		for i in range(len(array)-1-count):
			if array[i] > array[i+1]:
				array[i],array[i+1] = array[i+1],array[i]
				is_sorted = False
		count+=1
	return array