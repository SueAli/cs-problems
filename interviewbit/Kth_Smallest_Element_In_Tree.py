# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq
from collections import deque
class Solution:
    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    heap =[]
    def BFS( self, root):
        self.heap =[]
        q = deque()
        if not root:
            return
        q.append(root)
        while q:
            currNode = q.popleft()
            heapq.heappush(self.heap, currNode.val)
            if currNode.left: q.append(currNode.left)
            if currNode.right: q.append(currNode.right)
    def kthsmallest(self, root, k):
        self.BFS(root)
        if k > len(self.heap):
            return None
        i = 0
        while i < k:
            kth_item = heapq.heappop(self.heap)
            i += 1
        return kth_item


