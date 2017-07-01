## https://www.interviewbit.com/problems/nqueens/
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
class Pos:
    def __init__(self,r, c):
        self.row = r
        self.col = c
    def getRowRep(self, n):
        return "."*self.col +"Q"+"."*(n-self.col-1)

class Solution:
    # @param A : integer
    # @return a list of list of strings
    ### Time Complexity ??
    ### Space Compexity ???
    def solveNQueens(self, A):
        qPos = []
        result = []
        self.placeQueenRec(0,qPos,A,result)
        for s in result:
            for i in range (0,len(s)):
                s[i] = s[i].getRowRep(A)
        return result


    def placeQueenRec(self, curr_row, positions, n, result):
        if curr_row == n :
            result.append(positions[:])
            return True
        for col in range (0, n ):
            safeFlag = True
            for i in range (0, len(positions)):
                q = positions[i]
                if q.row == curr_row or \
                                q.col == col or \
                                        q.row + q.col == col+curr_row or \
                                        q.row - q.col == curr_row - col:
                    safeFlag = False
                    break
            if safeFlag:
                positions.append(Pos(curr_row,col))
                self.placeQueenRec(curr_row+1,positions,n,result)
                positions.pop()



