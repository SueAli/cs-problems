# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Time Complexity = O(n) because each node must visited once to invert its children
        Space Complexity = O(h) the function calls that will be added to stack (h is the length of the tree)
        h (0:n) --> Space complexity = O(n)
        """
        if root == None:
            return None
        tmp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tmp
        return root
