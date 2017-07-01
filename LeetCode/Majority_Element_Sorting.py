import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time Complexity = O(n + n*Log n ) = O (n)
        Space Complexity = O(1)
        """


        nums.sort() # n * log n

        curr_ocur = 0
        prev = None


        majorityElemCount = math.floor(len(nums)/2.0)

        i = 0
        while i < len(nums):
            if nums[i] == prev:
                curr_ocur += 1

            else:
                prev = nums[i]
                curr_ocur = 1

            if curr_ocur > majorityElemCount:
                    return prev

            i += 1



