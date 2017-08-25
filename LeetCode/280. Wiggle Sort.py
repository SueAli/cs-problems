# 280. Wiggle Sort
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        # O( n log n )
        nums.sort()
        n = len(nums)
        i = 1
        while i < n - 1:
            nums[i] , nums[i+1] = nums[i+1], nums[i]
            i += 2
        """
        # O(n) Time
        # O(1) Space complexity
        rel = 1
        for i in range(1,len(nums)):
            if (rel > 0 and nums[i] < nums[i-1]) or (rel < 0 and nums[i] > nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]
            rel *= -1



