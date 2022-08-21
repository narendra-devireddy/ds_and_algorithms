#o(n^2) time complexity | o(1) space
def longestPalindromicSubstring(string):
    # Write your code here.
    max_length = 1
    best_left = 0
    best_right = 1
    for i in range(1,len(string)-1):
      odd_left, odd_right = 0,0
      even_left, even_right = 0,0
      if string[i-1] != string[i+1] and \
          string[i] != string[i+1]:
          continue
      if string[i-1] == string[i+1]:
        left = i-1
        right = i+1
        odd_left, odd_right = get_palindrome_bounds(string,left,right)
      if string[i] == string[i+1]:
        left = i-1
        right = i+2
        even_left, even_right = get_palindrome_bounds(string,left,right)
      if max_length < odd_right-odd_left+1:
        max_length = odd_right-odd_left+1
        best_left = odd_left
        best_right = odd_right
      if max_length < even_right-even_left+1:
        max_length = even_right-even_left+1
        best_left = even_left
        best_right = even_right
    return string[best_left:best_right+1]


def get_palindrome_bounds(string,left,right):
  while left >= 0 and right < len(string):
    if string[left] == string[right]:
      left-=1
      right+=1
    else:
      break
  return left+1, right-1