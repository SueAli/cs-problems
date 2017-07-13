# Definition for a binary tree node.
# Sum Root to Leaf Numbers
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from  collections import deque
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        # Breadth first search  BFS
        # Time complexity is O(n) .. all nodes will be visited
        # Space Complexity is O(n) for the queue
        """
        res = 0
        if root :
            q = deque ()
            q.append((root,root.val )) # each element has two entries 1st entry is the node itself , 2nd entry is the number represented by the path from the root to current node
            while q:
                curr_node, curr_num = q.popleft()
                if not curr_node.left and not curr_node.right: # it is a leaf node , add the numnber to the final res value
                    res += curr_num
                    continue
                if curr_node.left:
                    q.append((curr_node.left, (curr_num * 10 ) + curr_node.left.val))
                if curr_node.right:
                     q.append((curr_node.right, (curr_num * 10 ) + curr_node.right.val))

        return res