# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys
class Solution:
    # @param A : root node of tree
    # @return an integer
    ### Time Complexity is O(n)
    ### Space Complexity is O( log n)
    def minDepth(self, A):
        def minDepRec(root, curDep):
            if not root:
                return sys.maxint
            curDep += 1
            if not root.left and not root.right:
                return curDep 
            leftDep = minDepRec(root.left, curDep)
            rightDep = minDepRec(root.right, curDep)
            return min(leftDep,rightDep)
        return minDepRec(A,0)