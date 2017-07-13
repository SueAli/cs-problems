# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#  Path Sum II
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        # Depth first search , Binary Tree
        # Time Complexity is O(n)
        # Space complexity avg O(log n ), worst O(n) for recursion stack size
        """
        final_res = []
        def pathSumDFS(root,target, curr_sum, curr_path):
            if root:
                curr_sum += root.val
                curr_path.append(root.val)
                if not root.left and not root.right:
                    if curr_sum == target:
                        final_res.append(curr_path[:])

                else:
                    if root.left :
                        pathSumDFS(root.left, target,curr_sum, curr_path)
                    if root.right:
                        pathSumDFS(root.right, target,curr_sum, curr_path)

                curr_path.pop()



        pathSumDFS(root,sum, 0 ,[])
        return final_res

