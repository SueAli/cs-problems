# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        nodes_val_list = []
        q = deque()
        q.append(root)
        nodes_val_list.append(root.val)
        while q:
            curr_len = len(nodes_val_list)
            j = curr_len - 1
            i = 0
            while i <= j:
                if nodes_val_list[i] != nodes_val_list[j]:
                    return False
                i += 1
                j -= 1

            nodes_val_list=[]
            for i in range (0, curr_len):
                curr_n = q.popleft()
                if curr_n.left:
                    q.append(curr_n.left)
                    nodes_val_list.append(curr_n.left.val)
                else:
                    nodes_val_list.append(None)
                if curr_n.right:
                    q.append(curr_n.right)
                    nodes_val_list.append(curr_n.right.val)
                else:
                    nodes_val_list.append(None)


        return True



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.rigt = TreeNode(3)

s = Solution()

print s.isSymmetric(root)
