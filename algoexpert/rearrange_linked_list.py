# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrangeLinkedList(head, k):
    # Write your code here.
    less_header = None
    less_tail = None
    greater_header = None
    greater_tail = None
    equal_header = None
    equal_tail = None
    ptr = head
    while ptr is not None:
      if ptr.value < k:
        less_header,less_tail = grow_linked_list(less_header,less_tail,ptr)
      elif ptr.value > k:
        greater_header,greater_tail = grow_linked_list(greater_header,greater_tail,ptr)
      else:
        equal_header,equal_tail = grow_linked_list(equal_header,equal_tail,ptr)
      prv_node = ptr
      ptr = ptr.next
      prv_node.next = None
    connected_header,connected_tail=connect_linked_list(less_header,less_tail,\
    													equal_header,equal_tail)
    connected_header,connected_tail=connect_linked_list(connected_header,connected_tail,\
    													greater_header,greater_tail)

    return connected_header



def grow_linked_list(header,tail,current_node):
    new_header = header
    new_tail = current_node
    if new_header is None:
      new_header = current_node
    if tail is not None:
      tail.next = new_tail
    return new_header,new_tail

def connect_linked_list(header1, tail1, header2, tail2):
	if header1 is None:
		return header2,tail2
	if header2 is None:
		return header1, tail1 
	tail1.next = header2
	return header1, tail2