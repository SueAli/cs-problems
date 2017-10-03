import sys
from collections import deque

class Solution(object):

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # time Complexity is O(n * m )
        # Space complexit is O(n*m) for the queue

        dir_ =[(0,-1), (0,1), (-1,0), (1,0)]

        rows = len(matrix)
        cols = len(matrix[0])
        q = deque()
        res =[[sys.maxint for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range ( cols):
                if matrix[i][j] == 0 :
                    q.append([ 0 ,(i,j)])
                    res[i][j] = 0

        while q:
            val, pos = q.popleft()
            r, c = pos[0], pos[1]
            for d in dir_:
                c_row = d[0] + r
                c_col = d[1] + c
                if 0<= c_row < rows and 0 <= c_col < cols :
                    if  res[c_row][c_col]==sys.maxint :
                        q.append ([matrix[c_row][c_col]+val ,(c_row,c_col)])
                    res[c_row][c_col] = min(val +matrix[c_row][c_col],  res[c_row][c_col])


        return res


