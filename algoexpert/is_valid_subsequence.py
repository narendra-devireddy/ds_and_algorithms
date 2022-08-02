##Given two non empty integer arrays
##determine if second array is subsequence of first
##Subsequence means numbers should appear in same order 
## A single number in array and array itself are also valid subsequence
#time complexity o(n) where n is len of array|o(1) space complexity
def isValidSubsequence(array, sequence):
	i=0
	j=0
	while j <len(sequence) and i<len(array):
		if sequence[j]==array[i]:
			j+=1
		i+=1
	return j==len(sequence)
