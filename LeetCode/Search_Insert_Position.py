class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## Time Complexity is O(n)
        i = len(nums)-1
        while i >= 0 and nums[i] > target:
            i -= 1

        if i >= 0 and nums[i] == target:
            return i
        else:
            return i +1


