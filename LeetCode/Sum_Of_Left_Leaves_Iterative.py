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
        Time Complexity = O(n) -> each node should be visited once
        Space Complexity = O(n) 
        """
        if root == None:
            return 0 
        s = 0
        dq = deque()
        dq.append(root)
        while(len(dq) > 0):
            curr = dq.popleft()
            if curr.left != None:
                if curr.left.left == None and curr.left.right == None:
                    s += curr.left.val
                else:
                    dq.append(curr.left)
            if curr.right != None:
                dq.append(curr.right)
        
        return s                
            