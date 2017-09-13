# Reverse Words in a String III
# Time Complexity is O(n)
# Space Comp is O(1)
# Easy
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = [c for c in s]
        i = 0

        while i < len(s):
            if s[i] == " ":
                i += 1
                continue

            j = i+1
            while j < len(s) and s[j] !=" ":
                j += 1

            new_i = j
            j -= 1

            while j > i :
                s[j], s[i] = s[i], s[j]
                i += 1
                j -= 1
            i = new_i

        return "".join(s)
        
