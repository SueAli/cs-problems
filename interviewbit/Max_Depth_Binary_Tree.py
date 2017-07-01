# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    ### Time Complexity is O(n)
    ### Space Compexity is O(log n )
    def maxDepth(self, A):
        def getMaxDepRec( root, currDepth):
            if not root:
                 return currDepth
            currDepth += 1
            leftDepth = getMaxDepRec(root.left, currDepth)
            rightDepth = getMaxDepRec(root.right, currDepth)
            return max(leftDepth,rightDepth)
        return getMaxDepRec(A,0)