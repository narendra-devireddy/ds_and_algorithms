# O(n) time complexity | O(1) space
# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    # Write your code here.
    orig_tail = head
    list_length = 1
    while orig_tail.next is not None:
      list_length+=1
      orig_tail=orig_tail.next

    modified_k = abs(k) % list_length

    if k >=0:
      offset = list_length - modified_k
    elif k < 0:
      offset = modified_k
    
    if offset == 0 or offset ==list_length:
      return head
    
    new_tail = head
    for i in range(offset-1):
      new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    orig_tail.next = head
    return new_head
      