# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Comp is O(log n )
# Space Comp is O( n ) # the len of str
class Solution(object):

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        def parseTree(root):
            res = ""
            if not root :
                return res

            res += str(root.val )
            if root.left or root.right :
                res = res + '(' + parseTree(root.left) + ')'
            if root.right:
                res = res + '(' + parseTree(root.right) + ')'
            return res
        return parseTree(t)

