class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_heap = [(0,0)]

        in_mst = [False] * n

        min_cost = 0
        points_connected = 0

        while points_connected < n:
            distance, current = heapq.heappop(min_heap)

            if in_mst[current]:
                continue

            in_mst[current] = True
            min_cost += distance
            points_connected += 1

            for i in range(n):
                if not in_mst[i]:
                    new_distance = (abs(points[current][0] - points[i][0]) + abs(points[current][1] - points[i][1]))

                    heapq.heappush(min_heap, (new_distance, i))

        return min_cost