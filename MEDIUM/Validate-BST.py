class BST:
    """
    Time : O(n) traversing every singe node
    Space: O(d), d is the deeph  of the tree store on the stack.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
	return helper(tree, float("-inf"), float("+inf"))

def helper(tree, minVal, maxVal):
	if tree == None:
		return True
	if tree.value < minVal or tree.value >= maxVal:
		return False
	return helper(tree.left, minVal, tree.value) and helper(tree.right, tree.value, maxVal)