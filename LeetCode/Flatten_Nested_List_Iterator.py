# Flatten Nested List Iterator
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.items_q = deque()
        for m in nestedList:
            self.buildQueue(m)


    def buildQueue(self, item ):
        if item.isInteger():
            self.items_q.append(item)
            return
        x = item.getList()
        if len(x) ==0:
            return
        for c in x:
            self.buildQueue(c)

    def next(self):
        """
        :rtype: int
        """
        return self.items_q.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.items_q:
            return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []# while i.hasNext(): v.append(i.next())