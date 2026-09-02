class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amt = [amount + 1] * (amount + 1)

        amt[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    amt[i] = min(amt[i], 1 + amt[i - coin])

        if amt[amount] < amount + 1:
            return amt[amount]
        else:
            return -1
        