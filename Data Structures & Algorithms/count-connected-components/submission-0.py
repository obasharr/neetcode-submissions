class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        counter = 0
        visited = [0] * n

        adj_list = [[] for _ in range(n)]

        for i in range(len(edges)):
            adj_list[edges[i][0]].append(edges[i][1])
            adj_list[edges[i][1]].append(edges[i][0])

        for i in range(n):
            if visited[i] == 0:
                counter += 1
                self.dfs(adj_list, visited, i)

        return counter

    def dfs(self, adj_list, visited, node):
        visited[node] = 1
        
        for i in range(len(adj_list[node])):
            if visited[adj_list[node][i]] == 0:
                self.dfs(adj_list, visited, adj_list[node][i])
