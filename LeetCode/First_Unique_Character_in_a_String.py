import sys
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        Time Complexity : O(n)
        Space Complexity: O(n)
        """
        if len(s) == 0:
            return -1

        hash_t = {}
        i = 0
        while i < len(s): #O(n)
            if s[i] in hash_t:
                hash_t[s[i]] = sys.maxint
            else:
                hash_t[s[i]] = i
            i += 1

        min_i = min(hash_t.values()) #O(n)

        if min_i == sys.maxint:
            return -1
        else:
            return min_i