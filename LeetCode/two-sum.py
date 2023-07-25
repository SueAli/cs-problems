
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        # brute force solution
        # Time complexity => O(n*2)
        # Space complexity => O(1)
        n = len(nums)
        for i in range (0, n):
            for j in range (i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # Time complexity is O(1)
        # Space complexity is O(n) for creating the dictionary
        n = len(nums)
        if n != 0:
            nums_dic = {}
            for i in range (0, n):
                nums_dic[nums[i]] = i

            for i in range(0, n):
                remaining = target - nums[i]
                if nums_dic.get(remaining) is not None\
                and nums_dic.get(remaining) != i :
                    return [i, nums_dic.get(remaining)]
        return []

