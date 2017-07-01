# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    # Time complexity is O( min(len(A), len(B)) )
    # Space complexity is O( min(len(A), len(B)) ) for stack functions call
    def isSameTree(self, A, B):
        if not A and not B:
            return True
        if not A or not B:
            return False
        return (A.val == B.val) and self.isSameTree(A.left,B.left) and self.isSameTree(A.right, B.right)
