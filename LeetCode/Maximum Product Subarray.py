class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity O(n)
        # Space complexity is O(1)
        n = len(nums)

        if n == 0 :
            return 1
        elif n == 1:
            return nums[0]
        else:
            h_prod = nums[0]
            l_prod = nums[0]
            f_res = nums[0]
            for i in range(1, n):
                l_prod , h_prod= min(nums[i]*l_prod, nums[i], nums[i]*h_prod), max(
                    nums[i]*l_prod, nums[i], nums[i]*h_prod)
                f_res = max(f_res, h_prod)
            return f_res


