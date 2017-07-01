# Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ### Time Complexity is O(log num)
        ## Space Complexity is O(1)
        l, r = 1,num
        while l <= r:
            mid = l + (r-l)/2
            t = mid * mid
            if t == num: return True
            elif t < num:
                l = mid+1
            else:
                r = mid - 1
        return False
