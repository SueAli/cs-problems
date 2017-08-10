# House Robber I

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time comp is O(n)
        Space is O(n) and can be constant if we only used two int variables
        """

        n = len(nums)
        max_data = [ 0 for i in range(n+ 1)]

        if n > 0 :
            max_data[0] = 0
            max_data[1] = nums[0]
            for i in range(1,n):
                max_data[i+1] = max(nums[i]+ max_data[i-1], max_data[i])
        return max_data[n]






