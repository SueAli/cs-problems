# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    # @param A : root node of tree
    # @param val1 : integer
    # @param val2 : integer
    # @return an integer
    ### Time Complexity is O(n)
    ### Space Complexity is O(n) , it can be solved in O(log n ) memory using recusrion
    def lca(self, A, val1, val2):
        BFS_q = deque()
        parents  = {} # parents hashtable is O(n) memory
        if not A: return -1
        BFS_q.append(A)
        parents[A.val] = -1
        val1_path = set()
        while BFS_q:
            curr = BFS_q.popleft()
            if curr.left:
                parents[curr.left.val] = curr.val
                BFS_q.append(curr.left)
            if curr.right:
                parents[curr.right.val] = curr.val
                BFS_q.append(curr.right)

        while val1 != -1 and val1 in parents :
            val1_path.add(val1)
            val1 = parents[val1]

        while val2 != -1 and val2 in parents and val2 not in val1_path:
            val2 = parents[val2]
        if val2 in val1_path:
            return val2
        else:
            return -1

