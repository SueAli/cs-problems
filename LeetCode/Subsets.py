# Subsets leetcode
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def subsetRec(nums,st,res,curr_sub):
            res.append(curr_sub[:])
            if st == len(nums):
                return
            for i in xrange(st,len(nums)):
                curr_sub.append(nums[i])
                subsetRec(nums,i+1,res,curr_sub)
                curr_sub.pop()
        subsetRec(nums,0,res,[])
        return res

