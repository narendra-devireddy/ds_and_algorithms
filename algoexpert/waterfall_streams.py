def waterfallStreams(array, source):
    # Write your code here.
  row_above = array[0][:]
  row_above[source] = -1
  for i in range(1,len(array)):
    current_row = array[i][:]
    for j in range(len(row_above)):
      water_value = row_above[j] if row_above[j] < 0 else 0
      # if no water, continue
      if water_value ==0:
        continue
      # if not a block, just carry forward the water
      if current_row[j] != 1:
        current_row[j] += water_value
        continue
      # if we hit a block, traverse array left and right
      water_split = water_value/2
      left=j-1
      while left >= 0:
        if row_above[left] == 1:
          break
        else:
          if current_row[left] == 1:
            left-=1
          else:
            current_row[left]+= water_split
            break
      ## right traversal
      right=j+1
      while right < len(current_row):
        if row_above[right] == 1:
          break
        else:
          if current_row[right] == 1:
            right+=1
          else:
            current_row[right]+= water_split
            break
    row_above = current_row
  return [-100*x for x in row_above]