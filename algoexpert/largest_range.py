#o(N) complexity and o(N) space
def largestRange(array):
    # Write your code here.
    range_dict = dict()
    best_left = None
    best_right = None
    max_diff = -1
    for elem in array:
      range_dict[elem]=False

    for elem in array:
      range_dict[elem]=True
      left_num = elem-1
      while range_dict.get(left_num,True)==False:
        range_dict[left_num]=True
        left_num-=1
      right_num=elem+1
      while range_dict.get(right_num,True)==False:
        range_dict[right_num]=True
        right_num+=1
      if max_diff < right_num-left_num-1:
        max_diff=right_num-left_num-1
        best_left = left_num+1
        best_right = right_num-1
    return [best_left,best_right]
