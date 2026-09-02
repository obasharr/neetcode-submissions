class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = Counter(tasks)

        max_heap = [-freq for freq in freq_map.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap:
            temp = []

            for _ in range(n + 1):
                if max_heap:
                    temp.append(heapq.heappop(max_heap))

            for freq in temp:
                freq += 1
                if freq < 0:
                    heapq.heappush(max_heap, freq)

            if max_heap:
                time += n + 1
            else:
                time += len(temp)

        return time