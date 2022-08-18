#o(n) space and time complexity
def reverseWordsInString(string):
    # Write your code here.
    i=len(string)-2
    result = []
    end = len(string)-1
    while i >=0:
      if string[i] == ' ':
        if string[i+1] == ' ':
          end = max(end,i)
          if i>0 and string[i-1] != ' ':
            start=i
            result.append(string[start:end])
            end=i-1
        else:
          start = i+1
          result.append(string[start:end+1])
          end=i-1
      i-=1
    result.append(string[0:end+1])
    print(result)
    return ' '.join(result)