# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    ## Time Complexity is O(n)
    ## Space Complexity is O(h) where h is the height of the input tree 
    def t2Sum(self, A, B):
       s_inorder = []
       s_reverse = []
       done1 = False
       done2 = False
       curr1 = A
       curr2 = A
       val1 = 0
       val2 = 0
       if not A:
           return False
       while True:
           while not done1:
               if curr1:
                   s_inorder.append(curr1)
                   curr1 = curr1.left
               else:
                    if s_inorder:
                        curr1= s_inorder.pop()
                        val1= curr1.val
                        curr1 = curr1.right
                    done1= True

           while not done2:
               if curr2:
                   s_reverse.append(curr2)
                   curr2 = curr2.right
               else:
                   if s_reverse:
                       curr2 = s_reverse.pop()
                       val2 = curr2.val
                       curr2 = curr2.left
                   done2 = True
           if val1 != val2 and val1+val2 == B:
               return 1
           elif val1+val2 < B:
               done1 = False
           elif val1 + val2 > B:
               done2 = False
           if val1 >= val2:
               return 0


