# Word Search
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# Backtracking  , DFS

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def  helperfn( visited, board, i, j , word, w):
            if w == len(word):
                return True

            if  i < 0 or i == len(board) or j <0 or j == len(board[0]) or board[i][j] != word[w] or visited[i][j] :
                return False

            visited[i][j] = True
            tmp =  ( helperfn( visited, board, i-1, j , word, w+1) or
                    helperfn( visited, board, i+1, j , word, w+1) or
                    helperfn( visited, board, i, j-1 , word, w+1) or
                    helperfn( visited, board, i, j +1 , word, w +1 ))
            visited[i][j] = False
            return tmp


        rows, cols = len(board), len(board[0])
        visited = [[False for x in xrange(0,cols)] for y in xrange(0,rows)]
        if not word:
            return True

        for i in xrange(0,rows):
            for j in xrange(0, cols):
                if helperfn( visited, board, i, j , word, 0):
                    return True

        return False





