#o(n) time complexity | o(1) space complexity
def isPalindrome(string):
    # Write your code here.
    begin = 0
    end = len(string)-1
    while begin < end:
      if string[begin] != string[end]:
        return False
      begin+=1
      end-=1
    return True