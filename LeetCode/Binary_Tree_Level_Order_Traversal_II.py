# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Time Complexity is O(n)
        Space Complexity is O(n):  the queue will have n/2 at maximum ~ O(n)  + resulted List memory which is O(n)
        """
        if not root:
            return []
        r_list =[]
        q = deque()
        q.append(root)
        while q : # O(n)
            r_list.append([])
            curr_len = len(q)
            for i in range(0, curr_len):
                curr_node = q.popleft() # O(1)
                r_list[len(r_list) -1].append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left) # O(1)
                if curr_node.right:
                    q.append(curr_node.right) # O(1)

        return list(reversed(r_list))








