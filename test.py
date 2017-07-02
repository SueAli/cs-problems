class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def threeSumRec(st,nums,res,curr_set):
            if len(curr_set) == 3:
                if sum(curr_set) == 0 :
                    res.append(curr_set[:])
                return
            if st >= len(nums):
                return

            for i in xrange(st,len(nums)):
                if i > st and nums[i] == nums[i-1]:
                    continue
                curr_set.append(nums[i])
                threeSumRec(i+1,nums,res,curr_set)
                curr_set.pop()

        if nums:
            nums.sort()
            threeSumRec(0,nums,res,[])
        return res

                