class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]

        result = []

        self.backtrack(board, 0, result)

        return result

    def backtrack(self, board, col, result):
        if col == len(board):
            result.append(self.construct(board))
            return
        
        for row in range(len(board)):
            if self.isValid(board, row, col):
                board[row][col] = 'Q'
                self.backtrack(board, col + 1, result)
                board[row][col] = '.'

    def isValid(self, board, row, col):
        for i in range(col):
            if board[row][i] == 'Q':
                return False
            
        i, j = row, col

        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = row, col

        while i < len(board) and j >= 0:
            if board[i][j] == 'Q':
                return False
            
            i += 1
            j -= 1

        return True

    def construct(self, board):
        result = []

        for row in board:
            result.append("".join(row))

        return result

        