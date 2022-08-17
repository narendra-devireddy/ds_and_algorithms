#O(n+m) time complexity|o(1) space
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    if headOne.value < headTwo.value:
      merged_list = headOne
      c1 = headOne
      c2 = headTwo
    else:
      merged_list = headTwo
      c1 = headTwo
      c2 = headOne
    while c1.next is not None and c2 is not None:
      while c1.next is not None and c1.next.value < c2.value:
        c1=c1.next
      if c1.next is not None:
        next1 = c1.next
        next2 = c2.next
        c1.next = c2
        c2.next = next1
        c1 = c2
        c2 = next2
    if c2 is not None:
      c1.next = c2
    return merged_list