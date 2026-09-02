class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        island = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    island += 1
                    self.dfs(i, j, grid)

        return island

    def dfs(self, row, col, grid):
        new_row = len(grid)
        new_col = len(grid[0])

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        if row < 0 or col < 0 or row >= new_row or col >= new_col or grid[row][col] == '0':
            return 

        grid[row][col] = '0'

        for d in directions:
            self.dfs(row + d[0], col + d[1], grid)