def moveElementToEnd(array, toMove):
    # Write your code here.
    tomove_idx=othernumber_idx=0
    while tomove_idx < len(array) and othernumber_idx <len(array):
      while tomove_idx < len(array) and array[tomove_idx]!=toMove:
        tomove_idx+=1
      othernumber_idx=tomove_idx+1
      while othernumber_idx <len(array) and array[othernumber_idx]==toMove:
        othernumber_idx+=1
      if tomove_idx < len(array) and othernumber_idx <len(array):
        array[tomove_idx],array[othernumber_idx] = array[othernumber_idx],array[tomove_idx]
    return array