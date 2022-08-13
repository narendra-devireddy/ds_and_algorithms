# o(n) time complexity|o(1) space
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    prev=head
    current=prev.next
    prev.next=None
    while current is not None:
      next = current.next
      current.next = prev
      prev = current
      current=next
    return prev
