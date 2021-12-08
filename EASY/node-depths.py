def nodeDepths(root):
    """
    Recursive
    Time: O(n), the three is balanced
    Space: O(k), k is the height of the binary tree 
    """
    def nodeDepthsHelper(root, d):
        if root is None:
            return 0
            return d + nodeDepthsHelper(root.left, d + 1) + nodeDepthsHelper(root.right, d + 1)
        return nodeDepthsHelper(root, 0)  


# This is the class of the input binary tree.
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
