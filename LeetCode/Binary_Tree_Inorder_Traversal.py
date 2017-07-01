#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def inorderTraversal(self, root):
        """
        Time complexity is O(n)
        the main idea is establishing a link between the root and the end or the most right element of the left subtree
        This can be done by traversing the left subtree and keep it linked to the root ( link the predecessor to the root)
        and eventually you will get back to thr root after finishing the left subtree.
        :type root: TreeNode
        :rtype: List[int]
        """
        r_list= []
        current = root
        while current:
            if not current.left:
                r_list.append(current.val)
                current= current.right
            else:
                pre = current.left
                # if left subtree does not have a right child, its root will be the predecessor
                while pre.right  and pre.right != current:
                    pre = pre.right

                if not pre.right:
                    pre.right = current
                    current = current.left

                else:
                    pre.right = None
                    r_list.append(current.val)
                    current = current.right
        return r_list

