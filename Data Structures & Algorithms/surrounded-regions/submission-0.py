class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
       
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n -1) and board[i][j] == 'O':
                    self.dfs(board, i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != 'O':
            return
        
        board[i][j] = 'T'

        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)




                 