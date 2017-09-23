# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

# Time Complexity is O(n)
# Space Complexity is O(n)

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

        i =0
        stack_  = []
        res = None
        is_list = False
        curr_val = ""
        neg = False

        while i < len(s)  :
            if s[i] == '[':
                stack_.append(NestedInteger())

            elif s[i] == "-":
                neg = True

            elif s[i] in ( "," , "]") : # add prev num to curr Nested Int List

                if curr_val:
                    stack_[-1].add(NestedInteger((-1 if neg else 1 ) * int(curr_val)))
                if s[i] == "]": # end of the list
                    t = stack_.pop()
                    if not stack_:
                        res = t
                        break

                    stack_[-1].getList().append(t)

                # Reset All attr
                curr_val = ""
                neg = False

            else: # it is a digit  # curr_val = 123
                curr_val += s[i]
            i+= 1

        if res:
            return res
        if curr_val :
            return NestedInteger((-1 if neg else 1 )*int(curr_val) )
        return NestedInteger()



