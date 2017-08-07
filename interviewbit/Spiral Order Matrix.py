# Spiral Order Matrix
# Time complexity is O( n * n )

import math
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        cycles_cnt  =int( math.ceil(float(A)/2))
        spiral = [[0 for i in range(A)] for j in range(A)]
        num = 1
        for c in range(cycles_cnt):
            row = c
            for  col in range(c,A-c):
                spiral[row][col] = num
                num += 1
            col = A-c-1
            for row in range(c+1,A-c-1):
                spiral[row][col] = num
                num += 1
            row = A-c-1
            for col in range(A-c-1,c,-1):
                spiral[row][col] = num
                num += 1
            col = c
            for row in range(A-c-1,c,-1):
                spiral[row][col] = num
                num += 1

        return spiral





