# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    ## Time Complexity is O(n)
    ## Space complexity is O( log n)
    def sumNumbers(self, A):
        self.curSum = 0
        def sumNumRec ( root, curNum):
            if not root:
                return
            curNum = (curNum *  10) + root.val
            if not root.left and not root.right:
                self.curSum += curNum
                return
            if root.left:
                sumNumRec( root.left, curNum )
            if root.right:
                sumNumRec ( root.right, curNum)
            return
        sumNumRec(A,0)
        return self.curSum % 1003


