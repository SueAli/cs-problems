# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Time Complexity is O(n)
        Space complexity is O(n) for the resulted list
        """
        # it can be solved using moris tree traversal method without stack
        r_list =[]
        curr = root
        while curr:
            r_list.append(curr.val)
            if not curr.left:
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                if not pred.right:
                    # Make the pred refere to what I need to go back to after finishing the left subtree
                    pred.right = curr.right
                    curr = curr.left
                else:
                    pred.right = None
                    curr= curr.right

        return r_list


