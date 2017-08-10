# Closest Binary Search Tree Value

# Time complexity is O(h) ~ height of the tree ~ O(log n)
# Space complexity is O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        ptr = root
        min_diff = sys.maxsize
        min_val = None
        while ptr :
            diff = abs(target-ptr.val)
            if diff < min_diff :
                min_diff = diff
                min_val = ptr.val
            if target == ptr.val:
                break
            elif target < ptr.val :
                ptr = ptr.left
            else:
                ptr = ptr.right
        return min_val
