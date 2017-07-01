import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Time complexity is O(N)
        ## Space Complexity is O(1)
        if not nums: return 0
        max_s = -1* sys.maxint
        cursum =0
        for i in xrange(len(nums)):
            cursum += nums[i]
            if cursum > max_s:
                max_s = cursum
            if cursum < 0 :
                cursum = 0
        return max_s