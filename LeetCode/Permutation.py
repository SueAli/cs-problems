#  Permutations # Backtracking 
# Time Complexity is O(n!)
# Space Complexity is O(1) excluding the space used for O/p

class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def getAllPerm(idx, nums, res):
            if idx >= len(nums):
                res.append(nums[:])
                return
            for j in range(idx, len(nums)):
                nums[idx],nums[j] = nums[j], nums[idx]
                getAllPerm(idx+1 ,nums, res )
                nums[idx], nums[j] = nums[j], nums[idx]
        getAllPerm(0,nums, res)
        return res
