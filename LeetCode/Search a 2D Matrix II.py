import bisect

# Time complexity is O( n + m log m )
# space complexity is O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """


        rows = len(matrix) if matrix else 0
        cols = len(matrix[0]) if rows != 0 else 0

        res = False
        if rows > 0 and cols > 0 :
            for r in range(rows): # n
                if matrix[r][0] <= target <= matrix[r][cols-1]: # exist in that row  # binary search that row
                    idx = bisect.bisect_right( matrix[r], target)  # m log m
                    if idx > 0  and  matrix[r][idx-1] == target:
                        res = True
        return res
