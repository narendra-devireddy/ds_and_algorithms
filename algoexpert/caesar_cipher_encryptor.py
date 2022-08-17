#o(n) time complexity | o(n) space
def caesarCipherEncryptor(string, key):
    # Write your code here.
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    string_list = list(string)
    for i,c in enumerate(string_list):
      pos = alphabets.index(c)
      new_pos = pos+key
      new_pos = new_pos % len(alphabets)
      string_list[i] = alphabets[new_pos]
    return ''.join(string_list)
