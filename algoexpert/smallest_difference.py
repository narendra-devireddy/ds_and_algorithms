def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    result = []
    one_idx=two_idx=0
    min_diff = float('inf')
    while one_idx < len(arrayOne) and two_idx < len(arrayTwo):
      abs_diff = abs(arrayOne[one_idx]-arrayTwo[two_idx])
      if abs_diff < min_diff:
        result=[arrayOne[one_idx],arrayTwo[two_idx]]
        min_diff = abs_diff
      if arrayOne[one_idx]<arrayTwo[two_idx]:
        one_idx+=1
      else:
        two_idx+=1
    return result