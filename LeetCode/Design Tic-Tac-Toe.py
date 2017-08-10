class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.antidiag = 0
        self.diag = 0
        self.cols =[ 0 for _ in range(n)]
        self.rows = [0 for _ in range(n)]

        self.n = n
        self.grid = [[ 0 for ii in range(n)] for jj in range(n)]



    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        Time complexity is O(1)
        but the space complexity is O(n )

        """
        add = 1 if player == 1 else -1
        if row == col :
            self.diag += add

        if row == self.n - col - 1:
            self.antidiag += add

        self.cols[col] += add
        self.rows[row] += add
        if (abs(self.diag) == self.n or
            abs(self. antidiag) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.rows[row]) == self.n ):
            return player
        return 0







# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)