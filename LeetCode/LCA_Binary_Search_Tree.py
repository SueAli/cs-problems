# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        Time Complexity: O(log n)
        Space complexity: extra memory for function call stack ~ the height of tree
            worest / average case ~  O(log n )

        """
        if not root or not p or not q:
            return None

        if  min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root



#Testing
root = TreeNode(2)
root.left = TreeNode(1)
s = Solution()
r = s.lowestCommonAncestor(root,TreeNode(0),TreeNode(1))
print r.val
