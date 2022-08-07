def isMonotonic(array):
    # Write your code here.
    if len(array)<=1:
      return True
    increasing=None
    for i in range(len(array)-1):
      if increasing is None:
        if array[i]>array[i+1]:
          increasing=False
        elif array[i]<array[i+1]:
          increasing=True
      if increasing and array[i]>array[i+1]:
        return False
      if not increasing and array[i]<array[i+1]:
        return False
    return True

## A much cleaner way to write the code

def isMonotonic(array):
    # Write your code here.
    if len(array)<=1:
      return True
    increasing=None
    for i in range(len(array)-1):
      if increasing is None:
        if array[i]>array[i+1]:
          increasing=False
        elif array[i]<array[i+1]:
          increasing=True
      if increasing and array[i]>array[i+1]:
        return False
      if not increasing and array[i]<array[i+1]:
        return False
    return True

