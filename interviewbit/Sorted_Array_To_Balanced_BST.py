# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import math
class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    ## Time Complexity is O(n)
    ## Space Complexity is O( log n )
    def sortedArrayToBST(self, A):
        def buildBST(arr, start, end):
            if start > end:
                return None
            mid = start+int(math.ceil((end-start)/2.))
            root = TreeNode(arr[mid])
            root.left = buildBST(arr, start, mid -1)
            root.right = buildBST(arr, mid+1, end)
            return root
        return buildBST(A,0,len(A)-1)
