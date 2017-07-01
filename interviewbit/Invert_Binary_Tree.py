# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root : root node of tree
    # @return the root node in the tree
    ## Time Complexity is O(n)
    ## Space Complexity is O(height of tree) for recursive functions call stack
    def invertTree(self, root):
        if not root:
            return
        tmp = root.right
        root.right = root.left
        root.left = tmp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
