# 3Sum 3 sum
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Time Complexity is O ( n * n )
        Space Complexity is O(1)
        """
        res = []
        if len(nums) >= 3 :
            nums.sort()

            for i in xrange(0,len(nums)-2):
                if i > 0 and nums[i] == nums[i-1]: # To skip duplicates start with same val
                    continue
                st = i+1
                end = len(nums)-1
                target = -nums[i]
                while st < end :
                    partial_s = nums[st] + nums[end]
                    if partial_s == target:
                        res.append([nums[i],nums[st],nums[end]])
                        #to skip duplicates having same 2nd item
                        while st < end and nums[st] == nums[st+1]:
                            st += 1
                        #to skip duplicates having same 3rd item
                        while st < end and nums[end] == nums[end-1]:
                            end -= 1
                        st += 1
                        end -= 1

                    elif partial_s < target:
                        st += 1
                    else:
                        end -= 1
        return res

