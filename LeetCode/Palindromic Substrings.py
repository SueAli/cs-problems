# Palindromic Substrings

# Time Complexity is O(n ^ 2)

class Solution(object):
    def getPalLen(self,start , end, s):
        cnt = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            cnt += 1
            start -= 1
            end  += 1
        return cnt

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        all_pal_cnt = 0
        for i in range(len(s)):
            all_pal_cnt += self.getPalLen(i,i,s) # odd pal
            all_pal_cnt += self.getPalLen(i,i+1,s) # even pal
        return all_pal_cnt