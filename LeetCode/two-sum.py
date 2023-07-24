
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
  # brute force solution
  # Time complexity => O(n*2)
  # Space complexity => O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range (0, n):
            for j in range (i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
