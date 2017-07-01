# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    # Time complexity is O(n)
    # Space complexity is O(n) ~ O(log n) the size of functions call stack + O(n/2) maximum length of the resulted list

    def binaryTreePaths(self, root):
        r_list =[]
        def findBinaryPaths(root, currStr):
            if not root:
                return
            if len(currStr) > 0 :
                currStr += "->"
            currStr += str(root.val)
            if not root.left and not root.right:
                r_list.append(currStr)
                return
            if root.left:
                findBinaryPaths(root.left, currStr)
            if root.right:
                findBinaryPaths(root.right,currStr)

        findBinaryPaths(root,"")
        return r_list





