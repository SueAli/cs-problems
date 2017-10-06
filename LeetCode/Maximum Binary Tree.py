# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        #time complexity is O(n log n )
        # space complexity is O( log n ) -- > worst case is O(n)
        """
        def addNode(root, node): # Time O(log(n)) # Space O( log n )
            if not root:
                return node
            if root.val < node.val :
                node.left = root
                root = node
            else:
                root.right = addNode(root.right, node)
            return root


        tree = None
        for num in nums: # time is O(n)
            tree = addNode(tree, TreeNode(num))
        return tree