# Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## Time Complexity is O(n)

        vowels ="aeiouAEIOU"
        s = list(s)
        i,j = 0, len(s)-1
        while i<j and i < len(s) and j >= 0:
            while i < j:
                if s[i]  in vowels:
                    break
                i += 1

            while j > i:
                if s[j]  in vowels:
                    break
                j -= 1

            if s[i] in vowels and s[j] in vowels:
                t = s[i]
                s[i] = s[j]
                s[j] = t
                i += 1
                j -= 1
            if i == j:
                break

        return "".join(s)