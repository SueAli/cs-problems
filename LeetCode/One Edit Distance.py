# leetcode One Edit Distance
# Time complexity is O(n)
# Space complexity is O(1)


class Solution(object):
    def isOneEditDistance(self, a, b):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        edits = 0
        i = 0
        j = 0
        while i < len(a) and j < len(b) :
            if a[i] == b[j]:
                i += 1
                j += 1
                continue
            edits += 1
            if len(a) == len(b): # replace on of them in a  or b to match the other one
                i += 1
                j += 1
            else:
                if len(a) < len(b): # insert chr to a
                    j += 1
                else:   # insert chr to b
                    i += 1

        if i < len(a) :
            edits += len(a) - i
        if j < len(b):
            edits += len(b) - j

        if edits == 1:
            return True
        return False



