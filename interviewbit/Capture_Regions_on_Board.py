# Capture Regions on Board
# https://www.interviewbit.com/problems/capture-regions-on-board/
from collections import deque
class Solution:
    # @param A : list of list of chars
    ### Time Complexity is (n*n)
    ### Space complexity is O(n*n)
    def solve(self, A):
        def solveRange(A,row_range,col_range):
            for i in row_range:
                for j in col_range:
                    if A[i][j] == 'O':
                        q = deque()
                        q.append((i,j))
                        while q:
                            curr_i, curr_j = q.popleft()
                            A[curr_i][curr_j]='B'
                            if curr_i != 0 and A[curr_i-1][curr_j] =='O':
                                q.append((curr_i-1,curr_j))
                            if curr_i != len(A)-1 and  A[curr_i+1][curr_j]=='O' :
                                q.append((curr_i+1,curr_j))
                            if curr_j != 0 and A[curr_i][curr_j-1] =='O' :
                                q.append((curr_i,curr_j-1))
                            if curr_j != len(A[0])-1 and A[curr_i][curr_j+1] =='O':
                                q.append((curr_i,curr_j+1))

        rows,cols = len(A),len(A[0])
        solveRange(A,(0,rows-1),range(0,cols))
        solveRange(A,range(0,rows),(0,cols-1))
        for i in range (0, rows):
            for j in range (0,cols):
                if A[i][j] =='O': A[i][j]='X'
                elif  A[i][j] =='B': A[i][j]='O'


