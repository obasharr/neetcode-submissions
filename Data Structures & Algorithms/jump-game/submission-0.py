class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= final:
                final = i

        if final == 0:
            return True
        else:
            return False