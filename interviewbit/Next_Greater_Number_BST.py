# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        curr = A
        prev = None

        while curr  :
            if curr.val == B: # Then the solution must be in the right subtree, the most left child in subtree
                curr = curr.right
                while curr:
                    prev = curr
                    curr = curr.left
                return prev

            elif curr.val > B:
                prev = curr
                curr = curr.left
            else:
                curr = curr.right

        return prev


n1 = TreeNode(100)
n1.left = TreeNode(98)
n1.right = TreeNode(102)

s = Solution()
m = s.getSuccessor(n1,97)

print m.val