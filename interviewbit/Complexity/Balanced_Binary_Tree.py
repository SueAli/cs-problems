# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    # Time Complexity is O (n)
    # Space Complexity is  O ( log n )
    def getHeight(self,root):
        if not root:
            return -1
        return max(self.getHeight(root.left),self.getHeight(root.right)) + 1


    def isBalanced(self, A):
        if not A:
            return True
        return abs(self.getHeight(A.left) - self.getHeight(A.right)) <= 1 and self.isBalanced(A.right) and self.isBalanced(A.left)

