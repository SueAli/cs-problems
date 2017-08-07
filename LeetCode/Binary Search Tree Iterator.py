#  Binary Search Tree Iterator
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.next_stack = []
        ptr = root
        while ptr :
            self.next_stack.append(ptr)
            ptr = ptr.left



    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.next_stack) > 0



    def next(self):
        """
        :rtype: int
        """
        curr_node = self.next_stack.pop()

        ptr =  curr_node.right
        while ptr :
            self.next_stack.append(ptr)
            ptr = ptr.left
        return curr_node.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())