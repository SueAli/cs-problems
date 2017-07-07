# Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        # Binary Tree , hash table , Recursive , Recursion
        # Time Complexity is O(n) # All nodes should  be visited
        # Space Complexity = O(n) for the hashtable + O(log n ) for recusive function stack = O(n)
        """
        def buildTreeRec(preorder, inorder, pre_st, pre_end, in_st, in_end,hash_t):
            #print  pre_st, pre_end, in_st, in_end
            if (pre_st < 0 or in_st < 0  or pre_end >=  len(preorder) or in_end >= len(inorder) or
                pre_st > pre_end or in_st > in_end):
                return None
            root = TreeNode(preorder[pre_st])
            idx_at_inorder =hash_t[root.val] #findRootIdx(inorder, in_st,in_end, root.val)
            root.left = buildTreeRec(preorder, inorder, pre_st+1 , pre_st + idx_at_inorder - in_st,in_st, idx_at_inorder - 1,hash_t)
            root.right = buildTreeRec(preorder, inorder, pre_st + idx_at_inorder - in_st+1, pre_end,idx_at_inorder+1, in_end ,hash_t)
            return root

        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        hash_t = { v:k for k,v in enumerate(inorder)}

        return buildTreeRec(preorder, inorder,0,len(preorder)-1, 0, len(inorder) -1,hash_t )
