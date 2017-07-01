class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        Given :len(s) = n & len(t) = m
            Time Complexity = O(n* log n + m* log m)
            Space complexity = O(n + m) ---> sorted function return list
        """
        return sorted(s) == sorted(t)