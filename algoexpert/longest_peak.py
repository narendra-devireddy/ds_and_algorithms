def longestPeak(array):
    # Write your code here.
  longest_peak = 0
  for i in range(1,len(array)-1):
  # find the peak
    if array[i] > array[i-1] and array[i] > array[i+1]:
  # get left side length
      j=i-1
      while j >0 and array[j] > array[j-1]:
        j-=1
  # get right side length
      k=i+1
      while k < len(array)-1 and array[k] > array[k+1]:
        k+=1
      longest_peak = max(longest_peak,k-j+1)
  return longest_peak