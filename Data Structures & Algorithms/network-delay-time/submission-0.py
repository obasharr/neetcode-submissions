class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create the graph as an adjacency list
        graph = defaultdict(list)

        for source, destination, weight in times:
            graph[source].append((destination, weight))

        # (distance, node)
        min_heap = [(0, k)]

        # Initialize distances with infinity
        distances = [float('inf')] * (n + 1)
        distances[k] = 0

        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)

            # Skip if we've already found a shorter path
            if current_dist > distances[current_node]:
                continue

            # Visit all neighbors
            for next_node, weight in graph[current_node]:
                next_dist = current_dist + weight

                if next_dist < distances[next_node]:
                    distances[next_node] = next_dist
                    heapq.heappush(min_heap, (next_dist, next_node))

        max_dist = max(distances[1:])

        return -1 if max_dist == float('inf') else max_dist