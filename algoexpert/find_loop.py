# O(n) time complexity|O(1) space
# a tricky question
# use two pointers, one traversing 1 node at a time
# other traversing two nodes at a time
# when they meet, essentially they are at a distance 
# from origin of loop the same as from beginning of linked list
# so after the meet, one pointer goes to head 
# both pointers travel one node at a time and when they meet
# that will be the origin of the loop
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
    p1 = head
    p2 = head 
    while True:
      p1 = p1.next
      p2 = p2.next.next
      if p1==p2:
        break
    p1 = head
    while p1!=p2:
      p1=p1.next
      p2=p2.next
    return p1