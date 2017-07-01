# 4 Sum problem leetcode
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

        Time Complexity is n ^ ( k - 1)

        """
        nums.sort()
        res = []
        def ksum( nums,k, target, p,res):

            if p == len(nums) or (nums[-1] * k) < target or (nums[p] * k) > target:
                return

            if k == 2:
                # base case
                i , j = p , len(nums) - 1
                while i < j :
                    if i >p  and nums[i] == nums[i-1]:
                        i += 1
                        continue
                    s = nums[i] + nums[j]
                    if s == target:
                        res.append([nums[i],nums[j]])
                        i += 1
                        j -= 1
                    elif s < target:
                        i += 1
                    else:
                        j -= 1
                return

            for i in xrange(p,len(nums)):
                if i > p and nums[i] == nums[i-1]:
                    continue
                before = len(res)
                ksum( nums,k-1, target-nums[i], i+1,res)
                after = len(res)
                added = after-before
                for l in xrange(-added,0,1):
                    res[l].append(nums[i])

        ksum( nums,4, target, 0,res)
        return res

s = Solution()
print s.fourSum([1,0,-1,0,-2,2],0)