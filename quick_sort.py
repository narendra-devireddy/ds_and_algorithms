#quicksort|o(nlogn) - avg. complexity|o(1) space
def quicksort(array, start_idx=0,end_idx=None):
	#if model called without end_idx, calculate it
	if end_idx is None:
		end_idx = len(array)-1
	#base case - if start > end, return 
	if start_idx >= end_idx:
		return
	#pivot is picked as start_index
	pivot = start_idx
	left=start_idx+1
	right=end_idx
	while left <= right:
		#if left > pivot and right < pivot, apt to swap 
		if array[pivot]<array[left] and array[pivot]>array[right]:
			array[left],array[right] = array[right],array[left]
		#if right is higher than pivot, move right pointer to left
		if array[right] >= array[pivot]:
			right-=1
		#if left is less than pivot, move left pointer to right
		if array[left] <= array[pivot]:
			left+=1
	#once we cross the left and right pointer, swap pivot with right pointer
	array[pivot],array[right]=array[right],array[pivot]
	#recursively call quicksort with right pointer as bisector 
	quicksort(array,start_idx,right-1)
	quicksort(array,right+1,end_idx)