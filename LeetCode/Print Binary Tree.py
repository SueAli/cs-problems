# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# n = d * ( 2**d  -1 )
## Time Coomp is O(n ) + O(log n ) = O( n )
## Space Complexity : avg O(log n ) , worst O(n) if the tree is right or left skewed
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return [""]

        def getDepth(root): # Time O(n) # Space avg O(log n) worst O(n)
            if not root:
                return 0
            return 1+ max(getDepth(root.left), getDepth(root.right))
        d = getDepth(root)

        mat = [["" for j in range( 2**d - 1 )] for i in range(d)]

        def fillMat (start, end, root, row):# Time O(log n) # Space avg O(log n) worst O(n)
            if not root:
                return
            mid = start + ((end - start) / 2)

            mat[row][mid] = str(root.val )
            fillMat(start,mid-1,root.left, row+1)
            fillMat(mid+1,end, root.right, row+1)

        fillMat (0, len(mat[0]) -1 , root, 0)
        return mat



