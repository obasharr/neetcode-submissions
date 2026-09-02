class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')] * n

        costs[src] = 0

        for i in range(k + 1):
            temp = costs.copy()
            for flight in flights:
                u = flight[0]
                v = flight[1]
                cost = flight[2]

                if costs[u] == float('inf'):
                    continue
                
                if temp[v] > costs[u] + cost:
                    temp[v] = costs[u] + cost

            costs = temp

        return -1 if costs[dst] == float('inf') else costs[dst] 

