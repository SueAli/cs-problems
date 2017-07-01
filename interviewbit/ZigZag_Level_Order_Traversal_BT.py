# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        r = []
        if not A:
            return r
        q = deque()
        q.append(A)
        read_from_left = True
        while q:
            n = len(q)
            tmp =[]
            for i in range(0,n):
                if read_from_left:
                    curr = q.popleft()
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)
                else:
                    curr = q.pop()
                    if curr.right: q.appendleft(curr.right)
                    if curr.left: q.appendleft(curr.left)
                tmp.append(curr.val)

            if tmp:
                r.append(tmp)
            read_from_left = not read_from_left
        return r
