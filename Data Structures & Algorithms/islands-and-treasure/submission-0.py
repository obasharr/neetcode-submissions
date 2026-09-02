class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [0, 1, 0, -1, 0]
        m = len(grid)
        n = len(grid[0])

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append([i, j])

        while queue:
            gate = queue.popleft()
            row = gate[0]
            col = gate[1]

            for i in range(4):
                new_row = row + dirs[i]
                new_col = col + dirs[i + 1]

                if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and grid[new_row][new_col] == 2147483647:
                    grid[new_row][new_col] = grid[row][col] + 1
                    queue.append([new_row, new_col])
