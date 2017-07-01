#Convert Sorted List to Binary Search Tree
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    # Time Complexity is O(n)
    # Space Complexity is O(n) +O(logn ) ~ O(n)
    def sortedListToBST(self, A):
        def BuildBSTRec(A,st,end):
            if st > end:
                return None
            mid = st + ((end -st)/2)
            root = TreeNode(A[mid])
            root.left = BuildBSTRec(A,st,mid-1)
            root.right = BuildBSTRec(A,mid+1,end)
            return root

        arr = []
        while A:
            arr.append(A.val)
            A = A.next
        return BuildBSTRec(arr,0,len(arr)-1)

