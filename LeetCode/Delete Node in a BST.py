# Delete Node in a BST
# Time complexity is O(log n )
# Space Complexity is O(log n )

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteHelper(self,root):
        new_root = None
        if not root.left:
            new_root = root.right
        elif not root.right:
            new_root = root.left
        else:
            left_sub = root.left
            new_root = root.right
            ptr = new_root
            while ptr.left:
                ptr = ptr.left
            ptr.left = left_sub
        return new_root

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root :
            return root
        if root.val == key :
            root = self.deleteHelper(root)
        elif root.val > key and root.left :
            root.left = self.deleteNode(root.left,key)
        elif root.val < key and root.right:
            root.right = self.deleteNode(root.right, key )
        return root
