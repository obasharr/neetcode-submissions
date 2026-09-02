class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        x = len(nums1)
        y = len(nums2)
        start = 0
        end = x
        while start <= end:
            part_x = (start + end) // 2
            part_y = (x + y + 1) // 2 - part_x
            x_left = float('-inf') if part_x == 0 else nums1[part_x - 1]
            x_right = float('inf') if part_x == x else nums1[part_x]
            y_left = float('-inf') if part_y == 0 else nums2[part_y - 1]
            y_right = float('inf') if part_y == y else nums2[part_y]
            if x_left <= y_right and y_left <= x_right:
                if (x + y) % 2 == 0:
                    return (max(x_left, y_left) + min(x_right, y_right)) / 2.0
                return max(x_left, y_left)
            elif x_left > y_right:
                end = part_x - 1
            else:
                start = part_x + 1
        return 0
        