class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        Time complexity : O(n)
        Space Complexity : O(1)
        """
        col_num = 0
        i = 0
        n = len(s)
        while i < n :
            col_num += (26 ** (n-i-1)) * ( ord(s[i]) - 64)
            i += 1
        return col_num