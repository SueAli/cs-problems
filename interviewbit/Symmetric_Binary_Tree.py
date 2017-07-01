# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    # Time Complexity is O(n)
    # Space complexity is O( height of Tree) ~ O (log n )
    def isSymmetric(self, A):
        s_in=[]
        s_rev=[]
        cur_in = A
        cur_rev = A
        val_in = 0
        done_in = False
        val_rev = 0
        done_rev = False
        while True :
            while not done_in:
                while cur_in :
                    s_in.append(cur_in)
                    cur_in = cur_in.left
                if s_in:
                    cur_in = s_in.pop()
                    val_in = cur_in.val
                    cur_in = cur_in.right
                done_in = True
            while not done_rev:
                while cur_rev:
                    s_rev.append(cur_rev)
                    cur_rev = cur_rev.right
                if s_rev:
                    cur_rev = s_rev.pop()
                    val_rev = cur_rev.val
                    cur_rev = cur_rev.left
                done_rev = True

            if not s_in and not s_rev:
                return 1

            elif (not s_in) or (not s_rev) or ( val_in != val_rev ) :
                return 0
            else:
                done_in = False
                done_rev = False

