def longestPalindromicSubstring(string):
    # Write your code here.
    max_length = 1
    best_left = 0
    best_right = 0
    for i in range(1,len(string)-1):
      if string[i-1] == string[i+1]:
        left = i-1
        right = i+1
      elif string[i] == string[i+1]:
        left = i-1
        right = i+2
      else:
        continue
      while left >= 0 and right < len(string):
        if string[left] == string[right]:
          left-=1
          right+=1
        else:
          break
      if max_length < (right-1)-(left+1)+1:
        max_length = right-(left+1)
        best_left = left+1
        best_right = right-1
    return string[best_left:best_right+1]
