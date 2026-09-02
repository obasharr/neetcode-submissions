class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

        for r in range(self.rows):
            for c in range(self.cols):
                if self.backtrack(r, c, word, 0):
                    return True

        return False
    
    def backtrack(self, row: int, col: int, word: str, index: int) -> bool:
        if index >= len(word):
            return True
        
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.board[row][col] != word[index]:
            return False
        
        rowdir = [0, 1, 0, -1]
        coldir = [1, 0, -1, 0]

        self.board[row][col] = '#'

        ret = False

        for d in range(4):
            ret = self.backtrack(row + rowdir[d], col + coldir[d], word, index + 1)
            if ret:
                break
        self.board[row][col] = word[index]
        return ret