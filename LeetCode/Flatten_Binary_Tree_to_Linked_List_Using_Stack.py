# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        Time complexity is O(n)
        Space complexity: best case ~(log n) and worest case is O(n) for the stack
        """
        curr = root
        s = []
        prev = None
        while curr or s:
           if curr:
               if curr.right:
                   s.append(curr.right)
               curr.right = curr.left
               curr.left = None
               prev = curr
               curr = curr.right
           else:
               curr = s.pop()
               prev.right = curr



