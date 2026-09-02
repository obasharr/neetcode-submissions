class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 0 or len(heights[0]) == 0:
            return []

        row = len(heights)
        col = len(heights[0])

        pacific_reachable = [[False] * col for _ in range(row)]
        atlantic_reachable = [[False] * col for _ in range(row)]

        for i in range(row):
            self.dfs(i, 0, pacific_reachable, heights)
            self.dfs(i, col - 1, atlantic_reachable, heights)

        for i in range(col):
            self.dfs(0, i, pacific_reachable, heights)
            self.dfs(row - 1, i, atlantic_reachable, heights)

        result = []

        for i in range(row):
            for j in range(col):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])

        return result

    def dfs(self, row, col, reachable, heights):
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        reachable[row][col] = True

        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]

            if new_row < 0 or new_row >= len(heights) or new_col < 0 or new_col >= len(heights[0]):
                continue
            
            if reachable[new_row][new_col]:
                continue
            
            if heights[new_row][new_col] >= heights[row][col]:
                self.dfs(new_row, new_col, reachable, heights)

