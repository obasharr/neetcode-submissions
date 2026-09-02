class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        max1 = nums[0]
        max2 = 0

        for i in range(len(nums) - 1):
            max1 = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = max1

        rob1 = 0
        rob2 = 0

        for i in range(1, len(nums)):
            max2 = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = max2

        return max(max1, max2)