class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while left < right:
            mid = (right + left) // 2
            if self.canFinish(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left

    def canFinish(self, piles: List[int], speed: int, h: int) -> bool:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed) 
        return hours <= h
        