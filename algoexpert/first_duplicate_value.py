def firstDuplicateValue(array):
    # Write your code here.
    for i in range(len(array)):
    	index = abs(array[i])-1
    	if array[index] < 0:
    		return abs(array[i])
    	array[index] = array[index]*-1
    return -1