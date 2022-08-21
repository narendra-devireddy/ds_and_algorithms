# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def zipLinkedList(linkedList):
    # Write your code here.
    # 1. find the middle node
    ptr1 = ptr2 = linkedList
    while ptr2 is not None:
      if ptr2.next is not None:
        ptr2 = ptr2.next.next
      else:
        ptr2 = None
      if ptr2 is not None:
        ptr1 = ptr1.next
    # It would be None when there is no middle
    # i.e. one node LL
    middle_node_header = ptr1.next
    ptr1.next = None
    if middle_node_header is not None:

      # 2. Reverse right side LL
      prv = middle_node_header
      current = middle_node_header.next
      middle_node_header.next = None
      while current is not None:
        next = current.next
        current.next = prv
        prv = current
        current = next
      reversed_middle_header = prv
  
      # 3. Merge two lists
      left_ptr = linkedList
      right_ptr = reversed_middle_header
      while left_ptr is not None and right_ptr is not None:
        left_current = left_ptr
        right_current = right_ptr
        left_ptr = left_ptr.next
        right_ptr = right_ptr.next
        left_current.next=right_current
        right_current.next = left_ptr
      
    return linkedList