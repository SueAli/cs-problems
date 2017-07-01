class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        def validateSudoku(A):
            flag = True

            for i in range(0, 9):
                row_set = set()
                for j in range(0,9):
                    if A[i][j] != ".":
                        if A[i][j] in row_set:
                            flag = False
                            break
                        else:
                            row_set.add(A[i][j])
                if not flag:
                    break
            if flag:
                for i in range(0, 9):
                    row_set = set()
                    for j in range(0,9):
                        if A[j][i] != ".":
                            if A[j][i] in row_set:
                                flag = False
                                break
                            else:
                                row_set.add(A[j][i])
                    if not flag:
                        break
            if flag:
                for row in range (0,7,3):
                    for col in range (0,7,3):
                        block_set = set()
                        for i_row in range (row , row+3):
                            for j_col in range (col, col+3):
                                if A[i_row][j_col] != ".":
                                    if A[i_row][j_col] in block_set:
                                        flag = False
                                        break
                                    else:
                                        block_set.add(A[i_row][j_col])
                        if not flag:
                            break
                    if not flag:
                        break

            return flag




        def findFirstEmptyCell(A):
            i = -1
            j = -1
            for row in range (0,7,3):
                for col in range (0,7,3):
                    for i_row in range (row , row+3):
                        for j_col in range (col, col+3):
                            if A[i_row][j_col] == ".":
                                i = i_row
                                j = j_col
                                break
                        if i != - 1 and j != -1:
                            break
                    if i != - 1 and j != -1:
                            break
                if i != - 1 and j != -1:
                            break
            return i,j

        def fillSudoku(A):
            #print A
            if  not validateSudoku(A):
                return False
            i,j = findFirstEmptyCell(A)
            if (i == -1 and j == -1):
                return True

            opt = 0
            options = [1,2,3,4,5,6,7,8,9]
            while opt < len(options) and A[i][j] =="." :
                A[i] = A[i][0:j]+str(options[opt])+A[i][j+1:]
                if fillSudoku(A):
                    break
                A[i] = A[i][0:j]+str(".")+A[i][j+1:]
                opt += 1
            if opt == len(options):
                return False
            return True

        fillSudoku(A)
        return A

A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]

#A =["534678912", "672195348", ".98....6." , "859761423",  "4..8.3..1", "713924856", "961537284", "287419635", "....8..79"]

s = Solution()
print s.solveSudoku(A)







