class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []

        for i in range(n):
            time = (target - position[i]) / speed[i]
            cars.append([position[i], time])

        cars.sort(reverse = True)

        count = 0
        prev_time = 0

        for pos, time in cars:
            if time > prev_time:
                count += 1
                prev_time = time
            
        return count
        

        