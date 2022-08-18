#o(n) time complexity | o(n) space
def runLengthEncoding(string):
    # Write your code here.
    result = []
    prv_c = string[0]
    counter=0
    for i,c in enumerate(string):
      if c != prv_c or counter==9:
        result.append(str(counter))
        result.append(prv_c)
        prv_c = c
        counter = 1
      else:
        counter+=1
    result.append(str(counter))
    result.append(c)
    return ''.join(result)
