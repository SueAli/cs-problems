import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Time Complexity is O( m * n )
        Space Complexity is O( m * n) --> could be done in O(n )
        """
        cache = {}
        def minPathSum(grid,i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            else:

                if i == len(grid) -1 and j == len(grid[0]) -1:
                    return grid[i][j]

                elif i == len(grid) or  j == len(grid[0]):
                    return sys.maxint
                else:
                    cache[(i,j)] = grid[i][j] + min(minPathSum(grid,i+1,j), minPathSum(grid,i,j+1))
                    return  cache[(i,j)]

        return minPathSum(grid,0,0)
