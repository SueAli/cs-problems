# Valid Sudoku
# hash table
# time complexity is O(n*n)
# Space complexity is O(n)
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        hash_t = set()
        # validate all rows
        for r in range(rows):
            hash_t.clear() # O(1)
            for c in range(cols):
                if board[r][c] == '.' :
                    continue

                if board[r][c] in hash_t:
                    return False
                hash_t.add(board[r][c])


        # validate all cols
        for c in range(cols):
            hash_t.clear()
            for r in range(rows):
                if board[r][c] == '.' :
                    continue

                if board[r][c] in hash_t :
                    return False
                hash_t.add(board[r][c])
        # validate all 9  squares

        c_inc = 0
        while c_inc < 3:
            for c in range(c_inc*3, (c_inc*3)+3): # 0, 3
                r_inc = 0
                while r_inc < 3:
                    hash_t.clear()
                    for c in range(c_inc*3, (c_inc*3)+3): # 0, 3
                        for r in range(r_inc*3 , 3+(r_inc*3)): # 0,3, 3,6, 6,9
                            if board[r][c] == '.' :
                                continue

                            if board[r][c] in hash_t:
                                return False

                            hash_t.add(board[r][c])
                    r_inc += 1

            c_inc += 1
        return  True




            