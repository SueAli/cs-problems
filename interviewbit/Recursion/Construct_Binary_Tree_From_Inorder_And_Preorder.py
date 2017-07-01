# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
## Time Complexity is O(n^2)
## Space Complexity is O(log n )
class Solution:
    # @param preorder : list of integers denoting preorder traversal of tree
    # @param inorder : list of integers denoting inorder traversal of tree
    # @return the root node in the tree
    def __init__(self):
        self.pre_index = 0

    def buildTree(self, preorder, inorder):
        def getRootIndex(in_st, in_end,val):
            for i in range (in_st, in_end+1):
                if inorder[i] == val:
                    return i
            return -1

        def buildRec(in_st, in_end):
            if in_end < in_st:
                return None
            root = TreeNode(preorder[self.pre_index])
            self.pre_index += 1
            root_i = getRootIndex(in_st, in_end, root.val)
            root.left = buildRec(in_st, root_i -1)
            root.right = buildRec ( root_i + 1, in_end)
            return root

        return buildRec(0,len(inorder)-1)

s = Solution()
A = [ 1,4,2,5,3]
B = [ 5,4,1,2,3]
r = s.buildTree(B,A)
print r.val