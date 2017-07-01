# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.curr = root
        self.s = []

    def traverse(self):
        while self.curr:
            self.s.append(self.curr)
            self.curr = self.curr.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        self.traverse()
        if self.s:
            return True
        return False

    # @return an integer, the next smallest number
    def next(self):
        tmp = self.s.pop()
        self.curr = tmp.right
        return tmp.val


# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
