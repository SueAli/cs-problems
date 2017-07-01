# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    # Time Complexity is O(n)
    # Space complexity is O( h^2) --> avg ~ O ( (log n)^2) --> worest case is O(n^2)
    #  O(h) for stack function calls and for each call extra memory for
    # the current path will be created with max size of O(h), where h is the height of tree

    def helpPathSum(self,root,B, t):
        if not root: return
        if root.val == B and not root.left and not root.right:
            self.l.append(t+[root.val])
            return True

        if root.left: self.helpPathSum(root.left, B-root.val, t+[root.val])
        if root.right: self.helpPathSum(root.right, B-root.val, t+[root.val])

    def pathSum(self, root, sum1):
        self.l = []
        self.helpPathSum(root,sum1,[])
        return self.l



n1 = TreeNode(5)
n1.left = TreeNode(4)
n1.left.left = TreeNode(11)
n1.left.left.left = TreeNode(7)
n1.left.left.right = TreeNode(2)

n1.right = TreeNode(8)
n1.right.left = TreeNode(13)
n1.right.right = TreeNode(4)
n1.right.right.left = TreeNode(5)
n1.right.right.right = TreeNode(1)




s = Solution()
print s.pathSum(n1,22)