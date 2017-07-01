#Island Perimeter
#https://leetcode.com/problems/island-perimeter/
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ## Time Complexity is O(4*h*w)~ O(h*w) in which h is the height and w is the width
        ## Space Complexity is O(1)
        p = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0: p += 1
                    if j == 0 or grid[i][j-1] == 0: p += 1
                    if i == len(grid)-1 or grid[i+1][j] == 0: p+=1
                    if j == len(grid[0])-1 or grid[i][j+1] == 0: p+= 1
        return p