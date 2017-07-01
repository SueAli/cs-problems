# Remove K Digits leetcode python solution
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        s = []
        res = "0"
        if k <= 0 :
            res = num
        else:
            for c in num:
                while s and k > 0 and int(c) < int(s[-1]):
                    s.pop()
                    k -= 1
                s.append(c)
            while s and k > 0 :
                s.pop()
                k -= 1
            if s and int(str(''.join(s))) >0  :
            	res = str(int(str(''.join(s))))
        return res

