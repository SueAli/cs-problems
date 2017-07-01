# Level Order
# https://www.interviewbit.com/problems/level-order/
# Using BFS
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
### Time Complexity is O(n)
### Space Complexity is O(n)
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        q = deque()
        res = []
        if not A: return res
        q.append(A)
        while q:
            curr_len = len(q)
            tmp =[]
            for i in range (0,curr_len):
                curr = q.popleft()
                tmp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if tmp:
                res.append(tmp[:])
        return res


