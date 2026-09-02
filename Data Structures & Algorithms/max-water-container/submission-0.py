class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        area = 0

        while left < right:
            temp = (right - left) * min(heights[left], heights[right])
            if temp > area:
                area = temp
            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1

        return area

        