#o(log(n)) time | o(1) space
def findClosestValueInBst(tree, target):
    # Write your code here.
    if tree.value == target:
      return tree.value
    min_diff = float('inf')
    best_value = None
    current_tree = tree
    while current_tree is not None:
      current_value = current_tree.value
      if current_tree.value > target:
        current_tree = current_tree.left
      elif current_tree.value <= target:
        current_tree = current_tree.right
      else:
        return current_value
      if min_diff > abs(target-current_value):
        min_diff = abs(target-current_value)
        best_value = current_value
    return best_value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None