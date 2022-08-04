def threeNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	results = list()
    for i in range(len(array)-1):
		current = array[i]
		left_ix = i+1
		right_ix = len(array)-1
		while left_ix < right_ix:
			sum_ = current+array[left_ix]+array[right_ix] 
			if sum_ < targetSum:
				left_ix+= 1
			elif sum_ > targetSum:
				right_ix-= 1
			else:
				results.append([current,array[left_ix],array[right_ix]])
				left_ix+= 1
				right_ix-= 1
	return results


#### Method 2
def threeNumberSum(array, targetSum):
    array.sort()
    # Write your code here.
    final_result=list()
    for i,value in enumerate(array):
      result_list=twoNumberSum(array,i,targetSum-value)
      if len(result_list)>0:
        final_result.extend(result_list)
    return final_result

def twoNumberSum(array,index,target):
    result=list()
    solution_set = set()
    for i in range(index+1,len(array)):
      elem = array[i]
      if target-elem in solution_set:
        solution_list = [array[index],
                         min(elem,target-elem),
                         max(elem,target-elem)]
        result.append(solution_list)
      else:
        solution_set.add(elem)
    return sorted(result,key=lambda x:x[1])
