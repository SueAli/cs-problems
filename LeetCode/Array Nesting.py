class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity is O(n)
        # Space Complexity is O(n)

        n = len(nums)
        cycles = [0 for i in range(n)]
        max_len = 0
        for k in range(n):
            if cycles[k] == 0:
                curr_cycle = set()
                p = k
                while p not in curr_cycle:
                    curr_cycle.add(p)
                    p = nums[p]
                curr_len = len(curr_cycle)
                max_len = max(max_len ,curr_len )
                for idx in curr_cycle:
                    cycles[idx] = curr_len
        return max_len
