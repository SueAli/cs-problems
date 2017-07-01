# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    # Time Complexity is O(n)
    # Space complexity is O(tree height ) : avg ~ O(log n) , worst case is O(n) in case of chain tree
    def inorderTraversal(self, A):
        r = []
        s = []
        root = A
        while root or len(s) > 0  :
            if root :
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                r.append(root.val)
                root = root.right
        return r
