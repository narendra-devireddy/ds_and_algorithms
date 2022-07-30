##insertion sort|o(1) space|o(n^2) complexity
def insertion_sort(array):
	#start from second element
	#we sort by fixing the left part of array progressively 
	#until we reach the end
	for i in range(1,len(array)):
		j = i 
		while j > 0 and array[j] < array[j-1]:
			array[j],array[j-1] = array[j-1],array[j]
			j-=1
	return array
