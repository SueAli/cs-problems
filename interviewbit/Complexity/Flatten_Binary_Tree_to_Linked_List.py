# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    # Time Comlexity is O ( n log n )
    # Space Complexity is O ( log n ) for recursive functions call stack
    def getMostRightNode(self,root):
        if not root.left and not root.right:
            return root
        elif root.right:
            return self.getMostRightNode(root.right)
        else:
            return self.getMostRightNode(root.left)
            
    def flatten(self, A):
        curr = A
        while curr:
            if not curr.right:
                curr.right = curr.left
            else:
                if curr.left:
                    mrn = self.getMostRightNode(curr.left)
                    mrn.left = curr.right 
                    curr.right = curr.left
            curr.left = None
            curr = curr.right    
        return A
