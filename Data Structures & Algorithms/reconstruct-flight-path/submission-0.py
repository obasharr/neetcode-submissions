class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for from_airport, to_airport in tickets:
            graph[from_airport].append(to_airport)

        for destinations in graph.values():
            destinations.sort()

        itinerary = []

        self.dfs("JFK", graph, itinerary)

        return itinerary
    
    def dfs(self, airport, graph, itinerary):
        destinations = graph.get(airport)

        while destinations and len(destinations) > 0:
            next_airport = destinations.pop(0)
            self.dfs(next_airport, graph, itinerary)

        itinerary.insert(0, airport)

        

