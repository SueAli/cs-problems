# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder : list of integers denoting inorder traversal
    # @param postorder : list of integers denoting postorder traversal
    # @return the root node in the tree
    # Time Complexity is O(n^2) we will visit all nodes and at each node we will find its index in the inorder tree
    # Space Complexity is O ( log n ) for recursive function calls stack

    def buildTree(self,inorder, postorder):
        def findIndex(val,in_st,in_end):
            for i in range(in_st, in_end+1):
                if inorder[i] == val:
                    return i
            return -1
        def buildHelp( in_st, in_end, p_st, p_end):
            if p_end < p_st or in_end < in_st:
                return None
            root = TreeNode(postorder[p_end])
            root_i = findIndex(root.val,in_st,in_end)
            root.left = buildHelp(in_st, root_i - 1, p_st, p_st + root_i - (in_st + 1))
            root.right = buildHelp(root_i + 1, in_end, p_st+ root_i - in_st, p_end-1)
            return root

        if len(inorder) == 0 or len(postorder)==0 or len(inorder ) != len(postorder):
            return None

        return buildHelp(0, len(inorder) -1 , 0 , len(postorder) -1 )


A = [ 17, 12, 24, 13, 2, 22, 9, 20, 18, 23, 3, 15, 21, 10, 4, 11, 19, 14, 16, 7, 1, 5, 6, 8 ]
B = [ 17, 13, 2, 22, 24, 18, 20, 9, 15, 3, 11, 4, 10, 14, 16, 19, 1, 7, 21, 23, 12, 6, 8, 5 ]

s = Solution()

n = s.buildTree(A,B)
