def findClosestValueInBst(tree, target):
    """
    Recursion, create a helper function wich will compute the closest value, if the diference of target number and closest is grather than the diference
    between the current value of the node. In that case set closest value to the current value of the tree.
    Then recursively update closest and discart left of right part of the tree if the values are far from the target.
    BigO:
    Time: O(log(n))
    Space: O(log(n))
    """
    closest = float('inf')
    return findClosestValueInBstHelper(tree, target, closest)
		
def findClosestValueInBstHelper(tree, target, closest):

	if tree == None:
		return closest

	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value

	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)

	elif target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	
	else:
		return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
