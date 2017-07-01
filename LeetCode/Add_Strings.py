# Add Strings
# https://leetcode.com/problems/add-strings/
# Time Complexity is O( max(n1,n2))
# Space Complexity is O( max(n1,n2))
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry,i,j = 0, len(num1)-1 , len(num2)-1
        res = []
        while i >= 0 or j >= 0:
            tmp = carry
            if i >= 0 :
                tmp += int(num1[i])
                i -= 1
            if j >= 0:
                tmp += int(num2[j])
                j -= 1
            res.append( str(tmp%10))
            carry = tmp/10
        if carry > 0 :
            res.append(str(carry))
        res.reverse()
        return "".join(res)

