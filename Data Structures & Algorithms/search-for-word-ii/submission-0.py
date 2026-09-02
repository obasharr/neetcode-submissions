class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root
            for letter in word:
                if letter not in node.children:
                    node.children[letter] = TrieNode()
                node = node.children[letter]
            node.word = word
        
        self.board = board
        self.answer = []

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in root.children:
                    self.backtracking(row, col, root)

        return self.answer

    def backtracking(self, row: int, col: int, parrent: TrieNode):
        letter = self.board[row][col]
        curr_node = parrent.children[letter]

        if curr_node.word is not None:
            self.answer.append(curr_node.word)
            curr_node.word = None

        self.board[row][col] = "#"

        row_offset = [-1, 0, 1, 0]
        col_offset = [0, 1, 0, -1]

        for i in range(4):
            new_row = row + row_offset[i]
            new_col = col + col_offset[i]
        
            if (
                0 <= new_row < len(self.board)
                and 0 <= new_col < len(self.board[0])
                and self.board[new_row][new_col] in curr_node.children
            ):
                self.backtracking(new_row, new_col, curr_node)

        self.board[row][col] = letter

        if not curr_node.children:
            del parrent.children[letter]




