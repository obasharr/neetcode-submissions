class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) <= 1:
            return 0

        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        rest = [0] * n

        buy[0] = -prices[0]
        sell[0] = 0
        rest[0] = 0

        for i in range(1, n):
            buy[i] = max(buy[i-1], rest[i-1] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            rest[i] = max(rest[i-1], sell[i-1])

        return max(sell[n-1], rest[n-1])
