#binary search of sorted array | o(logn) complexity | o(1) space
#this is an iterative approach for binary search
def binary_search(sorted_array,element):
	low = 0
	high = len(sorted_array)
	mid = (low+high)//2
	searching = True
	while low<high:
		if element > sorted_array[mid]:
			low = mid+1
		elif element < sorted_array[mid]:
			high = mid
		else:
			print('element found at {mid}'.format(mid=mid))
			return mid
		mid = (low+high)//2
	print('Element not found')
	return






