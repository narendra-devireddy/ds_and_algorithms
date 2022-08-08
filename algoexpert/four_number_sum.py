def fourNumberSum(array, targetSum):
    # Write your code here.
	pair_sums = dict()
	results = list()
	## we won't be doing anything for first and last element in array
	## so setting range for outer for loop accordingly
	for i in range(1,len(array)-1):
		# in forward pass, we would check if target- current sum 
		# exists in dictionary, if yes, append the quadrplets to the result
		for j in range(i+1,len(array)):
			current_sum = array[i]+array[j]
			diff = targetSum - current_sum 
			if diff in pair_sums:
				# there could be multiple pairs for a given sum
				# iterate through the value list
				for pair in pair_sums[diff]:
					results.append(pair+[array[i],array[j]])
		# in backward pass, we append the values to dictionary
		# this is done to avoid duplicating quadrplets based on the order
		for k in range(0,i):
			current_sum = array[i]+array[k]
			if current_sum not in pair_sums:
				pair_sums[current_sum]=[[array[k],array[i]]]
			else:
				pair_sums[current_sum].append([array[k],array[i]])
	return results