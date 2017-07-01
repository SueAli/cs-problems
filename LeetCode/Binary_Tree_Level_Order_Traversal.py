# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Time Complexity is O(n) where each node in the tree will be visited once
        Space Complexity is O(n) which is the maximum size for the external queue ( = n/2)
        """
        if not root:
            return [] 
        r_list = []
        q = deque()
        q.append(root)
        while q:
            r_list.append([])
            
            for i in range (0, len(q)):
                curr_node = q.popleft()
                r_list[len(r_list) - 1].append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                    
        return r_list
                
                
                
                
                