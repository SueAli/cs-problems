# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Overall Time complexity = O(n)
        Space Complexity:
            The worst case the queue will contain all nodes in the same level. For example: in full binary tree the
            leaf level has Ceil[n/2] leaves ==> O(n) node
        """
        if root == None:
            return None
        dq = deque()
        dq.append(root)
        while (len(dq) !=0):
            # pop current node to swap its children
            current = dq.popleft() #O(1) in douple linked list
            # swap children
            tmp = current.left
            current.left = current.right
            current.right = tmp
            # Add non None child to queue to swap its children
            if current.left != None:
                dq.append(current.left)
            if current.right != None:
                dq.append(current.right)
        return root
