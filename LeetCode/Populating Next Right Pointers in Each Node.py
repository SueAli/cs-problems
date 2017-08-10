# Populating Next Right Pointers in Each Node

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    # Time comp is O(N)
    # space comp is (1)
    
    def connect(self, root):
        l_start = root

        while l_start :
            curr = l_start
            while curr:
                if curr.left:
                    curr.left.next = curr.right
                if curr.right and curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            l_start = l_start.left




