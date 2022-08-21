# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    # Write your code here.
    ptr1 = head
    ptr2 = head.next
    left_list_head = ptr1
    right_list_head = ptr2
    left_list = ptr1
    right_list = ptr2
    while ptr1 is not None and ptr2 is not None:
      ptr1 = ptr2.next
      if ptr1 is not None:
        ptr2 = ptr1.next
      else:
        ptr2 = None

      left_list.next = ptr1
      right_list.next = ptr2
      left_list=left_list.next
      right_list = right_list.next

    ptr1 = left_list_head
    ptr2 = right_list_head
    if ptr2 is None:
      return ptr1
    while ptr1 is not None and ptr2 is not None:
      left_next = ptr1.next
      right_next = ptr2.next
      ptr2.next = ptr1
      if right_next is not None:
        ptr1.next = right_next
      ptr1 = left_next
      ptr2 = right_next
    return right_list_head



## Recursive approach

def nodeSwap(head):
    # Write your code here.
    if head is None or head.next is None:
      return head

    next_node = head.next
    head.next = nodeSwap(head.next.next)
    next_node.next = head
    return next_node
