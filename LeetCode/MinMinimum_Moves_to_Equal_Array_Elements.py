class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time complexity = O(n)  --> for min & sum operations 
        Space complexity = O(1)
        """
        return sum(nums) - (min(nums) * len(nums))