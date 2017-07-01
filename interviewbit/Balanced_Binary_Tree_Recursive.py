# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Time Complexity is O(n)
    # Space Complexity is O(log n)
    def getHeight(self,root):
        if not root:
            return 0
        l_h = 0
        r_h = 0
        l_h = self.getHeight (root.left)
        if l_h == -1 : return -1
        r_h = self.getHeight(root.right)
        if r_h  == -1: return -1
        if abs(l_h-r_h) > 1 :
            return -1
        else:
            return max(l_h,r_h) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        Time Coplexity is O(n^2)

        """
        return self.getHeight(root) != -1

