# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, root):
        # Time complexity is O(n)
        # Space Complexity is O(log n ) for the stack
        s = []
        r = []
        while root or s :
            while root is not None :
                if root.right:
                    s.append(root.right)
                s.append(root)
                root = root.left
            if s :
                root = s.pop()
                if s:
                    if root.right != s[len(s) -1]:
                        r.append(root.val)
                        root = None
                    else:
                        tmp = s.pop()
                        s.append(root)
                        root = tmp
                else:
                    r.append(root.val)
                    root=None

        return r


n1 = TreeNode(2)
n1.left = TreeNode(1)
n1.right = TreeNode(3)

s = Solution()
print s.postorderTraversal(n1)