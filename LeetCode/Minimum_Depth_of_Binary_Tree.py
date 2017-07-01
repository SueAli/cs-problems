#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque 
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Time complexity is O(n)
        Space Complexity O(n) which is the max size of the queue (n/2)
        """
        if not root:
            return 0
        q = deque()
        q.append(root)
        dep = 0 
        while q:
            dep += 1
            n = len(q)
            while n > 0 :
                curr_node = q.popleft()
                if not curr_node.left and not curr_node.right:
                    return dep
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                n -= 1
        return dep
            
            
        