class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Time Complexity is O(nlogn)
        ## Space Complexity is O(1)
        moves = 0
        if not nums:
            return moves
        nums.sort()
        mid = (len(nums)-1)/2
        for i in xrange(0,len(nums)):
            moves += abs(nums[mid] - nums[i])
        return moves