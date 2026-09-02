class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart = newInterval[0]
        newEnd = newInterval[1]
        left = 0
        right = len(intervals)

        output = []

        while left < right and newStart > intervals[left][0]:
            output.append(intervals[left])
            left += 1

        if not output or output[-1][1] < newStart:
            output.append(newInterval)
        else:
            interval = output.pop()
            interval[1] = max(interval[1], newEnd)
            output.append(interval)
        
        while left < right:
            interval = intervals[left]
            left += 1

            start = interval[0]
            end = interval[1]

            if output[-1][1] < start:
                output.append(interval)
            else:
                interval = output.pop()
                interval[1] = max(interval[1], end)
                output.append(interval)
        return output           
