#o(n) time complexity | o(n) space complexity
def longestSubstringWithoutDuplication(string):
    # Write your code here.
    start = 0
    last_seen_dict=dict()
    max_substring_length = -1
    best_left = 0
    best_right = 0
    i=0
    while i < len(string):
      if string[i] in last_seen_dict:
        end = i-1
        if end-start+1 > max_substring_length:
          max_substring_length = end-start+1
          best_left = start
          best_right = end
        i = last_seen_dict[string[i]]
        start = i+1
        last_seen_dict.clear()
      else:
        last_seen_dict[string[i]]=i
      i+=1
    if len(string)-start > max_substring_length:
      best_left = start
      best_right = len(string)-1
    return string[best_left:best_right+1]
