#o(n*wlogw) time complexity | o(wn) space complexity
def groupAnagrams(words):
    # Write your code here.
    anagram_dict = dict()
    result = []
    for word in words:
      sorted_word = ''.join(sorted(word))
      if sorted_word not in anagram_dict:
        anagram_dict[sorted_word]=[word]
      else:
        anagram_dict[sorted_word].append(word)

    for k,v in anagram_dict.items():
      result.append(v)
    return result