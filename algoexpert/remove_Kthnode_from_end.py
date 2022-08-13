# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    ptr1 = head 
    ptr2 = head
    i=0
    while ptr2 != None and i < k:
      ptr2=ptr2.next
      i+=1
    if ptr2 is not None:
      while ptr2.next!=None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    else:
      ptr1.value = ptr1.next.value
    temp = ptr1.next
    ptr1.next = temp.next
    temp.next=None
