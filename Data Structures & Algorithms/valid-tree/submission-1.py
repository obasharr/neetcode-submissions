class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        stack = []
        visited = set()

        stack.append(0)
        visited.add(0)

        while stack:
            node = stack.pop()
            for neighbor in adj_list[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                stack.append(neighbor)

        if len(visited) == n:
            return True

        return False