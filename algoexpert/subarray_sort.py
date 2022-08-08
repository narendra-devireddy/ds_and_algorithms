#o(n) complexity|o(1) space
def subarraySort(array):
    # Write your code here.
    min_out_of_order_element = float('inf')
    max_out_of_order_element = float('-inf')
    min_index = 0
    max_index = len(array)
    # in first pass get the pivots that are out of place
    # pivots could be in the beginning or end 
    # or in the middle
    for i in range(len(array)):
      if (i==0 and array[i] > array[i+1]) or \
         (i == len(array)-1 and array[i] < array[i-1]) or \
          (i>0 and array[i]<array[i-1]) or \
          (i<len(array)-1 and array[i] > array[i+1]):
        if min_out_of_order_element > array[i]:
          min_out_of_order_element = array[i]
          min_index = i
        if max_out_of_order_element < array[i]:
          max_out_of_order_element = array[i]
          max_index = i 
    # in prev loop we have collected the min and max elements out of order 
    # and their indices
    # if pivots were detected, run loop to get the right position for 
    # out of place elements
    if min_out_of_order_element < len(array) and max_out_of_order_element >=0:
      j= min_index-1
      while j >= 0 and array[j]> min_out_of_order_element:
        j-=1 
      k=max_index+1
      while k < len(array) and array[k]< max_out_of_order_element:
        k+=1 
      return (j+1,k-1)
      # already sorted list
    else:
      return (-1,-1)
          
