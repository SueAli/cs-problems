# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    ## Time Complexity is O(n^2)
    ## Speace Complexity is O( height of Tree) ~ O(log n)
    def buildTree(self, A):
        def getMaxIndex(st,end):
            max_index = st
            max_val = A[st]
            for i in range(st+1,end+1):
                if A[i] > max_val:
                    max_index= i
                    max_val = A[i]
            return max_index

        def buildTreeRec(st,end):
            if st > end :
                return None
            max_i = getMaxIndex(st,end)
            root = TreeNode(A[max_i])
            root.left = buildTreeRec ( st, max_i -1 )
            root.right = buildTreeRec ( max_i +1 , end)
            return root
        return buildTreeRec(0,len(A)-1)




