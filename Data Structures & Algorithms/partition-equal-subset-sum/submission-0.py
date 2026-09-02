class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0

        for num in nums:
            totalSum += num

        if totalSum % 2 != 0:
            return False

        target = totalSum // 2

        dp = [False] * (target + 1)

        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True

        return dp[target]