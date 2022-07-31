#merge sort|o(nlogn) complexity|o(n) space
def merge_sort(array):
	#base case of single element
	if len(array)==1:
		return array 
	low = 0
	high = len(array)
	mid = (low+high)//2
	left_array = array[low:mid]
	right_array = array[mid:high]
	return merge_sort_merger(merge_sort(left_array),merge_sort(right_array))

#function where sorted arrays get merged 
def merge_sort_merger(left,right):
	sorted_array = [None]*(len(left)+len(right))
	i=j=k=0
	while i<len(left) and j<len(right):
		if left[i]<right[j]:
			sorted_array[k]=left[i]
			i+=1
		else:
			sorted_array[k]=right[j]
			j+=1
		k+=1
	while i<len(left):
		sorted_array[k]=left[i]
		i+=1
		k+=1
	while j<len(right):
		sorted_array[k]=right[j]
		j+=1
		k+=1
	return sorted_array



