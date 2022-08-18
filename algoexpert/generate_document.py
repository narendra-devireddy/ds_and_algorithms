# o(c+d) time complexity | o(c) space complexity
def generateDocument(characters, document):
    # Write your code here.
    if document == "":
      return True

    char_dict = dict()
    for c in characters:
      if c in char_dict:
        char_dict[c]+=1
      else:
        char_dict[c] = 1

    for d in document:
      if d not in char_dict:
        return False
      char_dict[d]-=1
      if char_dict[d]<0:
        return False  
    return True
