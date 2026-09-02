class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        extNums = [0] * (n + 2)

        extNums[0] = 1
        extNums[n + 1] = 1

        for i in range(1, n + 1):
            extNums[i] = nums[i - 1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(1, n + 1):
            for left in range(1, n - length + 2):
                right = left + length - 1

                for i in range(left, right + 1):
                    coins = extNums[left - 1] * extNums[i] * extNums[right + 1]
                    coins += dp[left][i - 1] + dp[i + 1][right]
                    dp[left][right] = max(dp[left][right], coins)

        return dp[1][n]