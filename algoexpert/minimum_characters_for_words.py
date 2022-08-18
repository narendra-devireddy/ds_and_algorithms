#o(n*l) time complexity | o(c) space complexity
def minimumCharactersForWords(words):
    # Write your code here.
    char_dict = dict()
    result=[]
    for word in words:
      word_char_dict = dict()
      for c in word:
        if c not in word_char_dict:
          word_char_dict[c] = 1
        else:
          word_char_dict[c]+=1
      update_char_dict(word_char_dict, char_dict)
    for k,v in char_dict.items():
        for i in range(v):
          result.append(k)
    return result

def update_char_dict(word_dict, main_dict):
  for k,v in word_dict.items():
    if k in main_dict:
      main_dict[k]=max(v,main_dict[k])
    else:
      main_dict[k] = v