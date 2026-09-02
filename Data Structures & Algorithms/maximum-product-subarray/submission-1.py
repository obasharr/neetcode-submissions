class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minNum = nums[0]
        maxNum = nums[0]
        result = maxNum

        for i in range(1, len(nums)):
            current = nums[i]
            tempMax = max(current, maxNum * current, minNum * current)
            minNum = min(current, maxNum * current, minNum * current)
            maxNum = tempMax

            result = max(result, maxNum)

        return result
