# Inorder Successor in BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## Time complexity is O(h) ~ O(log n )
## Space complexity is O(1)

class Solution(object):
    def getSuccessor(self,root):
        successor = root
        while successor.left :
            successor = successor.left
        return successor


    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        ptr = root
        s = None
        prev_parent = None
        while ptr :
            print ptr.val
            if p.val == ptr.val : # node is found
                # case 1 : check the right tree
                if ptr.right :
                    s = self.getSuccessor(ptr.right)
                else:
                # case 2 : is the previous visited node that is greater than p
                    s = prev_parent
                break

            else:
                if ptr.val > p.val: # prev_parent val will only updated if it is greater than p
                    prev_parent = ptr

                if p.val < ptr.val :
                    ptr = ptr.left
                else:
                    ptr = ptr.right


        return s




