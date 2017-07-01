# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        Time complexity is O(n)
        Space complexity is O(log n) for the stack functions call
        """
        def sortedArrToBST(start,end):
            if end<start :
                return None
            root_index = start+ (end - start)/2
            root = TreeNode(nums[root_index])
            root.left = sortedArrToBST(start, root_index-1)
            root.right = sortedArrToBST(root_index+1,end)
            return root
        return  sortedArrToBST(0,len(nums)-1)
