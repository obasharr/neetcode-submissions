class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3

    def init(self, numCourses: int):
        self.isPossible = True
        self.color = {}
        self.adjList = {}
        self.topologicalOrder = []

        for i in range(numCourses):
            self.color[i] = self.WHITE

    def dfs(self, node: int):
        if not self.isPossible:
            return

        self.color[node] = self.GRAY

        for neighbor in self.adjList.get(node, []):
            if self.color[neighbor] == self.WHITE:
                self.dfs(neighbor)
            elif self.color[neighbor] == self.GRAY:
                self.isPossible = False

        self.color[node] = self.BLACK
        self.topologicalOrder.append(node)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.init(numCourses)

        for dest, src in prerequisites:
            if src in self.adjList:
                self.adjList[src].append(dest)
            else:
                self.adjList[src] = [dest]

        for i in range(numCourses):
            if self.color[i] == self.WHITE:
                self.dfs(i)

        if self.isPossible:
            order = []
            for i in range(numCourses):
                order.append(self.topologicalOrder[numCourses - i - 1])
            return order
        else:
            return []