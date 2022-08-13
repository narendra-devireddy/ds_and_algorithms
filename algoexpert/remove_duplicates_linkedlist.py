# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    ptr1 = linkedList
    while ptr1.next is not None:
      value = ptr1.value
      ptr2 = ptr1
      while ptr2.next is not None and ptr2.value == value:
        ptr2=ptr2.next
      ## if exited because of last node 
      ## check for the current value of ptr2
      if ptr2.value != value:
        ptr1.next = ptr2
        ptr1 = ptr2
      else:
        ptr1.next=None

    return linkedList