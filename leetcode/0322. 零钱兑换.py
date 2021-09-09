class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0: return 0
        dp = [0] + [amount + 1 for _ in range(amount)]

        for i in range(1, amount + 1):
            minCoin = amount + 1
            for coin in coins:
                if i >= coin:
                    minCoin = min(minCoin, dp[i - coin] + 1)
            dp[i] = minCoin
        return dp[amount] if dp[amount] < amount + 1 else -1
