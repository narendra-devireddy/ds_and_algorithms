#o(n) time complexity | o(n) space complexity
def firstNonRepeatingCharacter(string):
    # Write your code here.
    char_array = [0]*26
    for i,c in enumerate(string):
      array_ix = ord(c)-97
      char_array[array_ix]+=1

    for i,c in enumerate(string):
      pos_ix = ord(c)-97
      if char_array[pos_ix]==1:
        return i
    return -1
