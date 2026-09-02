class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum = 0

        for num in nums:
            sum += num

        if (target + sum) % 2 != 0 or sum < abs(target):
            return 0

        s1 = (target + sum) // 2

        if s1 < 0:
            return 0

        dp = [0] * (s1 + 1)
        dp[0] = 1

        for num in nums:
            for j in range(s1, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[s1]

        