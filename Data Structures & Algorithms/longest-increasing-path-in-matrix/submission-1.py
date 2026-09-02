class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        if len(matrix) == 0:
            return 0

        self.m = len(matrix)
        self.n = len(matrix[0])

        cache = [[0] * self.n for _ in range(self.m)]

        ans = 0

        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans, self.dfs(matrix, i, j, cache))

        return ans

    def dfs(self, matrix, i, j, cache):
        if cache[i][j] != 0:
            return cache[i][j]
        
        for d in self.dirs:
            x = i + d[0]
            y = j + d[1]

            if 0 <= x and x < self.m and 0 <= y and y < self.n and matrix[x][y] > matrix[i][j]:
                cache[i][j] = max(cache[i][j], self.dfs(matrix, x, y, cache))

        cache[i][j] += 1
        return cache[i][j]

