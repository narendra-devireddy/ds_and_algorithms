##function takes non empty array of distinct integers
##target sum
##if any two numbers of array sum to target, return in array
##if no two numbers sum to target return empty array
##order of numbers in array doesn't matter
def twoNumberSum(array, target):
	#store elements in a set for O(1) avg look up time
	set_store = set()
	for elem in array:
		if target-elem in set_store:
			return [elem,target-elem]
		else:
			set_store.add(elem)
	return []