# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        if not A:
            return  True

        if not A.left and not A.right:
            return True

        result = True

        if A.left:
            result = result and (A.left.val <= A.val) and self.isValidBST(A.left)

        if A.right:
            result = result and (A.right.val > A.val) and self.isValidBST(A.right)

        return result


n1 = TreeNode(11)
n1.left = TreeNode(4)
n1.left.left = TreeNode(5)
n1.left.right = TreeNode(1)
n1.right = TreeNode(2)
n1.right.left = TreeNode(5)


s = Solution()
m = int(s.isValidBST(n1))

print m