class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n * m - 1

        while left <= right:
            mid = (right + left) // 2
            mid_value = matrix[mid // n][mid % n]
            if mid_value ==  target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

        