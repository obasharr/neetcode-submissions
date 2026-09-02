class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        left = grid[0][0]
        right = n * n - 1

        while left < right:
            mid = left + (right - left) //  2

            if self.canSwim(grid, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def canSwim(self, grid, mid):
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        return self.dfs(grid, visited, 0, 0, mid)

    def dfs(self, grid, visited, i, j, mid):
        n = len(grid)

        if i < 0 or i >= n or j < 0 or j >= n or visited[i][j] or grid[i][j] > mid:
            return False
        if i == n - 1 and j == n - 1:
            return True

        visited[i][j] = True

        return self.dfs(grid, visited, i + 1, j, mid) or self.dfs(grid, visited, i - 1, j, mid) or self.dfs(grid, visited, i, j + 1, mid) or self.dfs(grid, visited, i, j - 1, mid)
