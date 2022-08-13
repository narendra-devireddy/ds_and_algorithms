#o(max(n,m)) time complexity|o(max(n,m)) space
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    result_linkedlist = None
    ptr_linkedlist1 = linkedListOne
    ptr_linkedlist2 = linkedListTwo
    extra_digit = 0
    while ptr_linkedlist1 is not None and ptr_linkedlist2 is not None:
      add1 = ptr_linkedlist1.value
      add2 = ptr_linkedlist2.value
      sum_ = add1+add2+extra_digit
      extra_digit = sum_//10
      sum_ = sum_ % 10
      if result_linkedlist is None:
        result_linkedlist = LinkedList(sum_)
        result_ptr = result_linkedlist
      else:
        result_ptr.next = LinkedList(sum_)
        result_ptr = result_ptr.next
      ptr_linkedlist1=ptr_linkedlist1.next
      ptr_linkedlist2=ptr_linkedlist2.next

    while ptr_linkedlist1 is not None:
      add1 = ptr_linkedlist1.value
      sum_ = add1+extra_digit
      extra_digit = sum_//10
      sum_ = sum_ % 10
      result_ptr.next = LinkedList(sum_)
      result_ptr = result_ptr.next
      ptr_linkedlist1=ptr_linkedlist1.next

    while ptr_linkedlist2 is not None:
      add2 = ptr_linkedlist2.value
      sum_ = add2+extra_digit
      extra_digit = sum_//10
      sum_ = sum_ % 10
      result_ptr.next = LinkedList(sum_)
      result_ptr = result_ptr.next 
      ptr_linkedlist2=ptr_linkedlist2.next
    if extra_digit !=0:
      result_ptr.next = LinkedList(extra_digit)
      result_ptr = result_ptr.next
    return result_linkedlist