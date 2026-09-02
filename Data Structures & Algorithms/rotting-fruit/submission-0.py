class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        fresh_count = 0

        rotten_queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten_queue.append([i, j])
        
        if fresh_count == 0:
            return 0

        minutes = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while rotten_queue:
            size = len(rotten_queue)
            for i in range(size):
                rotten = rotten_queue.popleft()
                for direction in directions:
                    x = rotten[0] + direction[0]
                    y = rotten[1] + direction[1]
                    if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh_count -= 1
                        rotten_queue.append([x, y])

            minutes += 1
        
        if fresh_count == 0:
            return minutes - 1
        else:
            return -1