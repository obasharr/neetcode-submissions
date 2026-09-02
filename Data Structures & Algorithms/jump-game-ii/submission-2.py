class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        curMax = 0
        curEnd = 0

        for i in range(len(nums) - 1):
            curMax = max(curMax, i + nums[i])
            if i == curEnd:
                jump += 1
                curEnd = curMax

        return jump