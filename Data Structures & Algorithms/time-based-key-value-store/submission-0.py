from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        arr = self.map[key]
        index = bisect_right(arr, (timestamp, chr(127))) - 1
        if index >= 0:
            return arr[index][1]
        return ""
