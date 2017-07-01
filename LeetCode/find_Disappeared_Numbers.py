#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Indexs can be used to mark the found numbers from 1 to n
        ### Time Complexity is O(n)
        ## Space Complexity is O(1)
        for item in nums:
            nums[abs(item) -1 ] = -1 * abs(nums[abs(item) -1])
        return [ i+1 for i,v in enumerate(nums) if v >0 ]



s = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print s.findDisappearedNumbers(nums)