# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time Complexity is O(n)
        # Space Complexity is O(n)
        steps ={0:1,1:1}
        if n in steps:
            return steps[n]
        for j in range(2,n+1):
            steps[j] = steps[j-1] + steps[j-2]
        return steps[n]

