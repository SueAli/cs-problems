# https://leetcode.com/problems/container-with-most-water/
# max area
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time O(n)
        # Space O(1)
        i , j = 0 , len(height)-1
        max_con = 0
        while i < j :
            max_con = max( max_con ,  (j -i) * min(height[i], height[j]) )
            if height[i] > height[j]:
                j -=1
            else:
                i += 1
        return max_con