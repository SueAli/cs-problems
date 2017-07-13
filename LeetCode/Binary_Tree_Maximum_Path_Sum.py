#Binary Tree Maximum Path Sum
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def __init__(self):
        self.max_sum = None # Anyting is greater than None

    def maxPathSum(self, root):

        """
        :type root: TreeNode
        :rtype: int
        Time Complexity is O(n)
        Space Complexity: ( for recursion stack space )
             Average is O(log n )
             Worst case is O(n)
        DFS , recursive

        """

        def max_path (root):
            if not root:
                return 0
            l = max_path(root.left)
            r = max_path(root.right)
            self.max_sum = max( self.max_sum,  root.val +l+r )
            return max(0 , root.val + max(l,r))

        max_path(root)
        return   self.max_sum
