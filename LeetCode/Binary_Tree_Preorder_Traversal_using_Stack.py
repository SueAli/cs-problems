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
        Space complexity is O(log n) for the stack +  O(n) return result container
        """
        r_list =[]
        if not root: return []
        stack = [root]
        while stack:
            curr = stack.pop()
            r_list.append(curr.val)
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)
        return r_list

