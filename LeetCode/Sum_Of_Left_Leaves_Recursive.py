# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Time Complexity => O(n)
        Space Complexity => O(n)
        """
        if root == None:
            return 0
        s = 0
        if root.left!= None:
            if root.left.left == None and root.left.right == None:
                s += root.left.val

            else:
                s += self.sumOfLeftLeaves(root.left)
        if root.right!= None:
            s += self.sumOfLeftLeaves(root.right)
        return s

