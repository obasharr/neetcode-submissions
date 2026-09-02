class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]

            root1 = self.find(parent, node1)
            root2 = self.find(parent, node2)

            if root1 == root2:
                return edge

            parent[root2] = root1

        return []

    def find(self, parent, node):
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node