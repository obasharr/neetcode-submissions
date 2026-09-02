class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        total = 0
        left_max = height[0]
        right_max = height[right]

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                if left_max - height[left] > 0:
                    total = total + left_max - height[left]
                left = left + 1
            else:
                right_max = max(right_max, height[right])
                if right_max - height[right] > 0:  
                    total = total + right_max - height[right] 
                right = right - 1

        return total