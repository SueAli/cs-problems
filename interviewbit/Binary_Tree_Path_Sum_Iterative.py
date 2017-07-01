# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    # Time Complexity is O(n)
    # Space Complexity is O( ceil(n/2)) ~ O(n)
    def hasPathSum(self, root, B):
        if not root: return False
        nodes = deque()
        sums = deque()
        nodes.append(root)
        sums.append(root.val)
        while nodes:
            node = nodes.popleft()
            curr_sum = sums.popleft()
            if curr_sum == B and not node.left and not node.right:
                return True
            if node.left:
                nodes.append(node.left)
                sums.append(curr_sum + node.left.val)
            if node.right:
                nodes.append(node.right)
                sums.append(curr_sum + node.right.val)
        return False


n1 = TreeNode(2)
n1.left = TreeNode(1)
n1.right = TreeNode(3)

s = Solution()
print s.hasPathSum(n1,5)