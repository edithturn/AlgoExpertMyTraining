class BinaryTree:
    """
    Recursion: Storage the sum of each node each time a node is visited.
    Then Do the same with left and finished with right nodes.
    Big(O):
    Time: O(n)
    Space: O(n)
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
	listSum = []
	sumSingleBranch(root, 0, listSum)
	return listSum

def sumSingleBranch(node, currentSum, listSum):
	
	if not node:
		return listSum
	
	newCurrentSum = currentSum + node.value
	
	if not node.left and not node.right:
		listSum.append(newCurrentSum)
    
	sumSingleBranch(node.left, newCurrentSum, listSum)
	sumSingleBranch(node.right, newCurrentSum, listSum)
    
